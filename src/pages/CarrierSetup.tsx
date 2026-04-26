import { useState, useEffect, useRef, useCallback } from 'react';
import { Upload, Trash2, CheckCircle, AlertCircle, Loader2, Pencil, Check, X, Search, ChevronDown, ChevronUp, FileText, RefreshCw, Eye, Play } from 'lucide-react';
import { api, Carrier } from '../services/api';

interface SpecStatus {
  total_files: number;
  reviewed_count: number;
  pending_count: number;
}


// ═══════════════════════════════════════════
// COMPONENT
// ═══════════════════════════════════════════
export default function CarrierSetup() {
  const [carriers, setCarriers] = useState<Carrier[]>([]);
  const [carrierName, setCarrierName] = useState('');
  const [labelSpec, setLabelSpec] = useState<File | null>(null);
  const [ediSpec, setEdiSpec] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  const [extractionStatus, setExtractionStatus] = useState<{ label?: string; edi?: string } | null>(null);

  // Rename state
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editName, setEditName] = useState('');
  const [renaming, setRenaming] = useState(false);

  // Search
  const [carrierSearch, setCarrierSearch] = useState('');

  // Expanded carrier + spec replacement
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [updatingSpec, setUpdatingSpec] = useState<{ carrierId: string; type: string } | null>(null);

  // PDF viewer
  const [viewingPdf, setViewingPdf] = useState<{ url: string; name: string } | null>(null);

  // Spec review status per carrier code
  const [specStatus, setSpecStatus] = useState<Record<string, { label?: SpecStatus; edi?: SpecStatus }>>({});
  // Rule generation loading
  const [generatingRules, setGeneratingRules] = useState<{ carrier: string; type: string } | null>(null);

  const labelRef = useRef<HTMLInputElement>(null);
  const ediRef = useRef<HTMLInputElement>(null);
  const replaceFileRef = useRef<HTMLInputElement>(null);
  const pendingReplace = useRef<{ carrierId: string; type: 'label' | 'edi' } | null>(null);

  useEffect(() => { loadCarriers(); }, []);

  const loadCarriers = async () => {
    try {
      const response = await api.listCarriers();
      if (response.success) setCarriers(response.carriers);
    } catch (error) {
      console.error('Failed to load carriers:', error);
    }
  };

  // Fetch spec file status when a carrier is expanded
  const fetchSpecStatus = useCallback(async (carrierCode: string) => {
    const status: { label?: SpecStatus; edi?: SpecStatus } = {};
    try {
      const labelRes = await api.getSpecFiles(carrierCode, 'label');
      if (labelRes.total_files !== undefined) {
        status.label = { total_files: labelRes.total_files, reviewed_count: labelRes.reviewed_count, pending_count: labelRes.pending_count };
      }
    } catch { /* no label specs */ }
    try {
      const ediRes = await api.getSpecFiles(carrierCode, 'edi');
      if (ediRes.total_files !== undefined) {
        status.edi = { total_files: ediRes.total_files, reviewed_count: ediRes.reviewed_count, pending_count: ediRes.pending_count };
      }
    } catch { /* no edi specs */ }
    setSpecStatus(prev => ({ ...prev, [carrierCode]: status }));
  }, []);

  // When carrier is expanded, fetch spec status
  useEffect(() => {
    if (expandedId) {
      const carrier = carriers.find(c => c._id === expandedId);
      if (carrier) fetchSpecStatus(carrier.carrier);
    }
  }, [expandedId, carriers, fetchSpecStatus]);

  // Generate rules handler
  const handleGenerateRules = async (carrierCode: string, specType: 'label' | 'edi') => {
    setGeneratingRules({ carrier: carrierCode, type: specType });
    try {
      const res = await api.generateRules(carrierCode, specType, false);
      if (res.success) {
        setMessage({
          type: 'success',
          text: `Generated ${res.rules_generated} ${specType} rules for ${carrierCode}. ${res.mongo_saved ? 'Saved to database.' : ''}`,
        });
        fetchSpecStatus(carrierCode);
        loadCarriers();
      } else {
        setMessage({ type: 'error', text: res.message || 'Rule generation failed' });
      }
    } catch {
      setMessage({ type: 'error', text: 'Failed to generate rules. Check server logs.' });
    } finally {
      setGeneratingRules(null);
    }
  };

  const filteredCarriers = carriers.filter(c =>
    c.carrier.toLowerCase().includes(carrierSearch.toLowerCase().trim())
  );


  // ─── Helper: get filename from path ───
  const getFileName = (path?: string) => {
    if (!path) return null;
    return path.split('/').pop() || path.split('\\').pop() || path;
  };

  // ─── View PDF ───
  const handleViewPdf = (specPath: string, specName: string) => {
    const url = `http://localhost:8000/api/carriers/files/${encodeURIComponent(specPath)}`;
    setViewingPdf({ url, name: specName });
  };

  // ─── Replace spec: trigger file picker ───
  const startReplaceSpec = (carrierId: string, type: 'label' | 'edi') => {
    pendingReplace.current = { carrierId, type };
    setTimeout(() => replaceFileRef.current?.click(), 50);
  };

  // ─── Replace spec: handle file selected ───
  const handleReplaceFileSelected = async (file: File) => {
    if (!pendingReplace.current) return;
    const { carrierId, type } = pendingReplace.current;
    pendingReplace.current = null;

    // Derive carrier code from carrier name
    const carrier = carriers.find(c => c._id === carrierId);
    const carrierCode = carrier?.carrier || carrierId;

    setUpdatingSpec({ carrierId, type });
    try {
      const response = await api.extractCarrierSpec(carrierCode, file, type);
      if (response.success) {
        setMessage({
          type: 'success',
          text: `${type.toUpperCase()} spec re-extracted for '${carrierCode}'. Review updated spec files in VS Code.`,
        });
        loadCarriers();
      } else {
        setMessage({ type: 'error', text: response.detail || response.message || `Failed to re-extract ${type} spec` });
      }
    } catch {
      setMessage({ type: 'error', text: 'Failed to re-extract spec file' });
    } finally {
      setUpdatingSpec(null);
    }
  };


  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!carrierName.trim()) { setMessage({ type: 'error', text: 'Please enter a carrier name' }); return; }
    if (!labelSpec && !ediSpec) { setMessage({ type: 'error', text: 'Please upload at least one specification file' }); return; }

    setUploading(true); setMessage(null); setExtractionStatus(null);
    const status: { label?: string; edi?: string } = {};
    let anyError = false;

    try {
      if (labelSpec) {
        const res = await api.extractCarrierSpec(carrierName.trim(), labelSpec, 'label');
        if (res.success) {
          status.label = res.spec_dir || 'extracted';
        } else {
          anyError = true;
          setMessage({ type: 'error', text: `Label extraction failed: ${res.detail || res.message || 'Unknown error'}` });
        }
      }

      if (ediSpec && !anyError) {
        const res = await api.extractCarrierSpec(carrierName.trim(), ediSpec, 'edi');
        if (res.success) {
          status.edi = res.spec_dir || 'extracted';
        } else {
          anyError = true;
          setMessage({ type: 'error', text: `EDI extraction failed: ${res.detail || res.message || 'Unknown error'}` });
        }
      }

      if (!anyError) {
        setExtractionStatus(status);
        setMessage({
          type: 'success',
          text: `Extraction & spec generation complete for '${carrierName}'. Review .md files in VS Code, then click "Generate Rules".`,
        });
        setCarrierName(''); setLabelSpec(null); setEdiSpec(null);
        if (labelRef.current) labelRef.current.value = '';
        if (ediRef.current) ediRef.current.value = '';
        loadCarriers();
      }
    } catch {
      setMessage({ type: 'error', text: 'Upload failed. Check server connection.' });
    } finally {
      setUploading(false);
    }
  };

  const handleDelete = async (carrierId: string, name: string) => {
    if (!confirm(`Delete carrier '${name}'?`)) return;
    try { await api.deleteCarrier(carrierId); setMessage({ type: 'success', text: `Carrier '${name}' deleted successfully` }); if (expandedId === carrierId) setExpandedId(null); loadCarriers(); }
    catch { setMessage({ type: 'error', text: 'Failed to delete carrier' }); }
  };

  const startEditing = (carrier: Carrier) => { setEditingId(carrier._id); setEditName(carrier.carrier); };
  const cancelEditing = () => { setEditingId(null); setEditName(''); };
  const handleRename = async (carrierId: string) => {
    const trimmed = editName.trim(); if (!trimmed) return;
    setRenaming(true);
    try { const response = await api.renameCarrier(carrierId, trimmed); if (response.success) { setMessage({ type: 'success', text: `Carrier renamed to '${trimmed}'` }); setEditingId(null); setEditName(''); loadCarriers(); } else { setMessage({ type: 'error', text: response.error || 'Rename failed' }); } }
    catch { setMessage({ type: 'error', text: 'Failed to rename carrier' }); }
    finally { setRenaming(false); }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Carrier Setup</h1>
          <p className="text-gray-600">Upload carrier specifications to create validation rule templates</p>
        </div>

        {message && (
          <div className={`mb-6 p-4 rounded-lg flex items-center gap-2 ${message.type === 'success' ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800'}`}>
            {message.type === 'success' ? <CheckCircle className="w-5 h-5" /> : <AlertCircle className="w-5 h-5" />}
            <span>{message.text}</span>
          </div>
        )}

        {/* Extraction path info */}
        {extractionStatus && (
          <div className="mb-6 p-4 rounded-lg bg-blue-50 text-blue-800 text-sm space-y-1">
            <p className="font-medium">Spec files generated — review in VS Code:</p>
            {extractionStatus.label && <p className="font-mono text-xs break-all">Label specs: {extractionStatus.label}</p>}
            {extractionStatus.edi && <p className="font-mono text-xs break-all">EDI specs: {extractionStatus.edi}</p>}
            <p className="text-blue-600 mt-1">After reviewing .md files, expand the carrier below and click "Generate Rules".</p>
          </div>
        )}

        {/* PDF Viewer Modal */}
        {viewingPdf && (
          <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-lg shadow-xl w-full max-w-4xl h-[80vh] flex flex-col">
              <div className="flex items-center justify-between p-4 border-b border-gray-200">
                <div className="flex items-center gap-2">
                  <FileText className="w-5 h-5 text-[#4a4337]" />
                  <h3 className="font-semibold text-gray-900">{viewingPdf.name}</h3>
                </div>
                <button onClick={() => setViewingPdf(null)} className="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors">
                  <X className="w-5 h-5" />
                </button>
              </div>
              <div className="flex-1 p-1">
                <iframe src={viewingPdf.url} className="w-full h-full rounded border border-gray-200" title={viewingPdf.name} />
              </div>
            </div>
          </div>
        )}

        {/* Hidden file input for spec replacement */}
        <input ref={replaceFileRef} type="file" accept=".pdf" className="hidden" onChange={(e) => { const file = e.target.files?.[0]; if (file) handleReplaceFileSelected(file); e.target.value = ''; }} />

        {/* Side by side */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Upload New Carrier */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold mb-4">Upload New Carrier</h2>
            <form onSubmit={handleUpload} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Carrier Name</label>
                <input type="text" value={carrierName} onChange={(e) => setCarrierName(e.target.value)} className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#4a4337] focus:border-transparent" placeholder="e.g., DHL, UPS, FedEx" />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Label Specification (PDF)</label>
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-4 hover:border-[#4a4337] transition-colors">
                  <input ref={labelRef} type="file" accept=".pdf" onChange={(e) => setLabelSpec(e.target.files?.[0] || null)} className="w-full" />
                  {labelSpec && <p className="mt-2 text-sm text-green-600 flex items-center gap-2"><CheckCircle className="w-4 h-4" />{labelSpec.name}</p>}
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">EDI Specification (PDF)</label>
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-4 hover:border-[#4a4337] transition-colors">
                  <input ref={ediRef} type="file" accept=".pdf" onChange={(e) => setEdiSpec(e.target.files?.[0] || null)} className="w-full" />
                  {ediSpec && <p className="mt-2 text-sm text-green-600 flex items-center gap-2"><CheckCircle className="w-4 h-4" />{ediSpec.name}</p>}
                </div>
              </div>
              <button type="submit" disabled={uploading} className="w-full bg-[#4a4337] text-white py-3 rounded-lg font-medium hover:bg-[#3a3529] disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center gap-2">
                {uploading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Upload className="w-5 h-5" />}
                {uploading ? 'Uploading, Extracting & Generating Specs...' : 'Upload Carrier Specs'}
              </button>
            </form>
          </div>

          {/* Configured Carriers */}
          <div className="bg-white rounded-lg shadow p-6 flex flex-col">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold">Configured Carriers</h2>
              {carriers.length > 0 && <span className="text-sm text-gray-500">{carriers.length} total</span>}
            </div>

            {carriers.length > 0 && (
              <div className="relative mb-4">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                <input type="text" value={carrierSearch} onChange={(e) => setCarrierSearch(e.target.value)} placeholder="Search carriers..." className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-[#4a4337] focus:border-transparent placeholder:text-gray-400" />
                {carrierSearch && <button onClick={() => setCarrierSearch('')} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"><X className="w-4 h-4" /></button>}
              </div>
            )}

            {carriers.length === 0 ? (
              <div className="text-center py-12 text-gray-500 flex-1 flex flex-col items-center justify-center">
                <p>No carriers configured yet</p>
                <p className="text-sm mt-2">Upload a carrier specification to get started</p>
              </div>
            ) : filteredCarriers.length === 0 ? (
              <div className="text-center py-12 text-gray-500 flex-1 flex flex-col items-center justify-center">
                <p className="text-sm">No carriers matching "{carrierSearch}"</p>
              </div>
            ) : (
              <div className="carrier-scroll space-y-3 overflow-y-auto flex-1 pr-1" style={{ maxHeight: '500px' }}>
                <style>{`
                  .carrier-scroll::-webkit-scrollbar { width: 6px; }
                  .carrier-scroll::-webkit-scrollbar-track { background: #f5f3f0; border-radius: 3px; }
                  .carrier-scroll::-webkit-scrollbar-thumb { background: #4a4337; border-radius: 3px; }
                  .carrier-scroll::-webkit-scrollbar-thumb:hover { background: #3a3529; }
                  .carrier-scroll { scrollbar-width: thin; scrollbar-color: #4a4337 #f5f3f0; }
                `}</style>

                {filteredCarriers.map((carrier) => {
                  const isExpanded = expandedId === carrier._id;
                  const isUpdating = updatingSpec?.carrierId === carrier._id;

                  return (
                    <div key={carrier._id} className={`border rounded-lg transition-colors ${isExpanded ? 'border-[#4a4337] bg-[#faf9f7]' : 'border-gray-200 hover:border-[#4a4337]'}`}>
                      {/* Carrier Row */}
                      <div className="flex items-center justify-between p-4">
                        {editingId === carrier._id ? (
                          <div className="flex items-center gap-2 flex-1 mr-2">
                            <input type="text" value={editName} onChange={(e) => setEditName(e.target.value)} onKeyDown={(e) => { if (e.key === 'Enter') handleRename(carrier._id); if (e.key === 'Escape') cancelEditing(); }} autoFocus className="flex-1 px-3 py-1.5 border border-[#5a5347] rounded-lg text-sm focus:ring-2 focus:ring-[#4a4337] focus:border-transparent" />
                            <button onClick={() => handleRename(carrier._id)} disabled={renaming || !editName.trim()} className="p-1.5 text-green-600 hover:bg-green-50 rounded-lg transition-colors disabled:opacity-50" title="Save">
                              {renaming ? <Loader2 className="w-4 h-4 animate-spin" /> : <Check className="w-4 h-4" />}
                            </button>
                            <button onClick={cancelEditing} className="p-1.5 text-gray-400 hover:bg-gray-50 rounded-lg transition-colors" title="Cancel"><X className="w-4 h-4" /></button>
                          </div>
                        ) : (
                          <>
                            <button onClick={() => setExpandedId(isExpanded ? null : carrier._id)} className="flex items-center gap-2 flex-1 text-left">
                              {isExpanded ? <ChevronUp className="w-4 h-4 text-[#4a4337]" /> : <ChevronDown className="w-4 h-4 text-gray-400" />}
                              <h3 className="font-medium text-gray-900">{carrier.carrier}</h3>
                            </button>
                            <div className="flex items-center gap-1">
                              <button onClick={() => startEditing(carrier)} className="p-2 text-gray-400 hover:text-[#4a4337] hover:bg-[#f5f3f0] rounded-lg transition-colors" title="Rename"><Pencil className="w-4 h-4" /></button>
                              <button onClick={() => handleDelete(carrier._id, carrier.carrier)} className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors" title="Delete"><Trash2 className="w-4 h-4" /></button>
                            </div>
                          </>
                        )}
                      </div>

                      {/* Expanded Detail */}
                      {isExpanded && (
                        <div className="px-4 pb-4 border-t border-gray-200 pt-3 space-y-3">
                          {/* Label Spec Row */}
                          <div className="flex items-center justify-between p-3 bg-white rounded-lg border border-gray-200">
                            <div className="flex items-center gap-2 flex-1 min-w-0">
                              <FileText className="w-4 h-4 text-[#4a4337] flex-shrink-0" />
                              <div className="min-w-0">
                                <p className="text-xs font-medium text-gray-500 uppercase tracking-wide">Label Spec</p>
                                <p className="text-sm text-gray-900 truncate">
                                  {getFileName(carrier.label_spec_path) || <span className="text-gray-400 italic">Not uploaded</span>}
                                </p>
                              </div>
                            </div>
                            <div className="flex items-center gap-1 flex-shrink-0 ml-2">
                              {carrier.label_spec_path && (
                                <button onClick={() => handleViewPdf(carrier.label_spec_path!, getFileName(carrier.label_spec_path) || 'Label Spec')} className="p-1.5 text-[#4a4337] hover:bg-[#f5f3f0] rounded-lg transition-colors" title="View PDF"><Eye className="w-4 h-4" /></button>
                              )}
                              <button onClick={() => startReplaceSpec(carrier._id, 'label')} disabled={isUpdating} className="p-1.5 text-[#4a4337] hover:bg-[#f5f3f0] rounded-lg transition-colors disabled:opacity-50" title={carrier.label_spec_path ? 'Replace & re-learn' : 'Upload label spec'}>
                                {isUpdating && updatingSpec?.type === 'label' ? <Loader2 className="w-4 h-4 animate-spin" /> : <RefreshCw className="w-4 h-4" />}
                              </button>
                            </div>
                          </div>

                          {/* EDI Spec Row */}
                          <div className="flex items-center justify-between p-3 bg-white rounded-lg border border-gray-200">
                            <div className="flex items-center gap-2 flex-1 min-w-0">
                              <FileText className="w-4 h-4 text-[#4a4337] flex-shrink-0" />
                              <div className="min-w-0">
                                <p className="text-xs font-medium text-gray-500 uppercase tracking-wide">EDI Spec</p>
                                <p className="text-sm text-gray-900 truncate">
                                  {getFileName(carrier.edi_spec_path) || <span className="text-gray-400 italic">Not uploaded</span>}
                                </p>
                              </div>
                            </div>
                            <div className="flex items-center gap-1 flex-shrink-0 ml-2">
                              {carrier.edi_spec_path && (
                                <button onClick={() => handleViewPdf(carrier.edi_spec_path!, getFileName(carrier.edi_spec_path) || 'EDI Spec')} className="p-1.5 text-[#4a4337] hover:bg-[#f5f3f0] rounded-lg transition-colors" title="View PDF"><Eye className="w-4 h-4" /></button>
                              )}
                              <button onClick={() => startReplaceSpec(carrier._id, 'edi')} disabled={isUpdating} className="p-1.5 text-[#4a4337] hover:bg-[#f5f3f0] rounded-lg transition-colors disabled:opacity-50" title={carrier.edi_spec_path ? 'Replace & re-learn' : 'Upload EDI spec'}>
                                {isUpdating && updatingSpec?.type === 'edi' ? <Loader2 className="w-4 h-4 animate-spin" /> : <RefreshCw className="w-4 h-4" />}
                              </button>
                            </div>
                          </div>

                          {/* Spec Review Status + Generate Rules */}
                          {(() => {
                            const cs = specStatus[carrier.carrier];
                            const labelSt = cs?.label;
                            const ediSt = cs?.edi;
                            const isGenLabel = generatingRules?.carrier === carrier.carrier && generatingRules?.type === 'label';
                            const isGenEdi = generatingRules?.carrier === carrier.carrier && generatingRules?.type === 'edi';
                            return (
                              <>
                                {/* Label Spec Files Status + Generate Rules */}
                                {carrier.label_spec_path && (
                                  <div className="flex items-center justify-between p-3 bg-[#faf9f7] rounded-lg border border-gray-200">
                                    <div>
                                      <p className="text-xs font-medium text-gray-500 uppercase tracking-wide">Label Spec Files</p>
                                      {labelSt && labelSt.total_files > 0 ? (
                                        <p className="text-sm text-gray-900">
                                          <span className={labelSt.reviewed_count === labelSt.total_files ? 'text-green-600 font-medium' : 'text-amber-600'}>
                                            {labelSt.reviewed_count}/{labelSt.total_files} reviewed
                                          </span>
                                          {labelSt.pending_count > 0 && <span className="text-gray-500 ml-1">({labelSt.pending_count} pending)</span>}
                                        </p>
                                      ) : (
                                        <p className="text-xs text-gray-400 italic">Spec files not generated yet</p>
                                      )}
                                    </div>
                                    {carrier.has_label_rules ? (
                                      <div className="flex items-center gap-1.5 px-3 py-1.5 text-sm">
                                        <CheckCircle className="w-3.5 h-3.5 text-green-600" />
                                        <span className="text-green-700 font-medium">Rules Generated</span>
                                        <button
                                          onClick={() => handleGenerateRules(carrier.carrier, 'label')}
                                          disabled={isGenLabel || isGenEdi}
                                          className="ml-2 p-1 text-gray-400 hover:text-[#4a4337] hover:bg-[#f5f3f0] rounded transition-colors disabled:opacity-50"
                                          title="Re-generate rules"
                                        >
                                          {isGenLabel ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <RefreshCw className="w-3.5 h-3.5" />}
                                        </button>
                                      </div>
                                    ) : (
                                      <button
                                        onClick={() => handleGenerateRules(carrier.carrier, 'label')}
                                        disabled={isGenLabel || isGenEdi}
                                        className="flex items-center gap-1.5 px-3 py-1.5 bg-[#4a4337] text-white text-sm rounded-lg hover:bg-[#3a3529] disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                                      >
                                        {isGenLabel ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Play className="w-3.5 h-3.5" />}
                                        {isGenLabel ? 'Generating...' : 'Generate Label Rules'}
                                      </button>
                                    )}
                                  </div>
                                )}

                                {/* EDI Spec Files Status + Generate Rules */}
                                {carrier.edi_spec_path && (
                                  <div className="flex items-center justify-between p-3 bg-[#faf9f7] rounded-lg border border-gray-200">
                                    <div>
                                      <p className="text-xs font-medium text-gray-500 uppercase tracking-wide">EDI Spec Files</p>
                                      {ediSt && ediSt.total_files > 0 ? (
                                        <p className="text-sm text-gray-900">
                                          <span className={ediSt.reviewed_count === ediSt.total_files ? 'text-green-600 font-medium' : 'text-amber-600'}>
                                            {ediSt.reviewed_count}/{ediSt.total_files} reviewed
                                          </span>
                                          {ediSt.pending_count > 0 && <span className="text-gray-500 ml-1">({ediSt.pending_count} pending)</span>}
                                        </p>
                                      ) : (
                                        <p className="text-xs text-gray-400 italic">Spec files not generated yet</p>
                                      )}
                                    </div>
                                    {carrier.has_edi_rules ? (
                                      <div className="flex items-center gap-1.5 px-3 py-1.5 text-sm">
                                        <CheckCircle className="w-3.5 h-3.5 text-green-600" />
                                        <span className="text-green-700 font-medium">Rules Generated</span>
                                        <button
                                          onClick={() => handleGenerateRules(carrier.carrier, 'edi')}
                                          disabled={isGenLabel || isGenEdi}
                                          className="ml-2 p-1 text-gray-400 hover:text-[#4a4337] hover:bg-[#f5f3f0] rounded transition-colors disabled:opacity-50"
                                          title="Re-generate rules"
                                        >
                                          {isGenEdi ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <RefreshCw className="w-3.5 h-3.5" />}
                                        </button>
                                      </div>
                                    ) : (
                                      <button
                                        onClick={() => handleGenerateRules(carrier.carrier, 'edi')}
                                        disabled={isGenLabel || isGenEdi}
                                        className="flex items-center gap-1.5 px-3 py-1.5 bg-[#4a4337] text-white text-sm rounded-lg hover:bg-[#3a3529] disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                                      >
                                        {isGenEdi ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Play className="w-3.5 h-3.5" />}
                                        {isGenEdi ? 'Generating...' : 'Generate EDI Rules'}
                                      </button>
                                    )}
                                  </div>
                                )}

                                {/* No specs uploaded yet */}
                                {!carrier.label_spec_path && !carrier.edi_spec_path && !isUpdating && (
                                  <p className="text-xs text-gray-400 italic px-1">No spec files yet. Upload a PDF above to start.</p>
                                )}
                              </>
                            );
                          })()}

                          {/* Re-learning indicator */}
                          {isUpdating && (
                            <div className="flex items-center gap-2 p-3 bg-[#f5f3f0] rounded-lg text-sm text-[#4a4337]">
                              <Loader2 className="w-4 h-4 animate-spin" />
                              <span>Extracting & generating specs from new {updatingSpec?.type} PDF...</span>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            )}

            {carrierSearch && filteredCarriers.length > 0 && (
              <p className="mt-3 text-xs text-gray-400 text-center">Showing {filteredCarriers.length} of {carriers.length} carriers</p>
            )}
          </div>
        </div>

      </div>
    </div>
  );
}