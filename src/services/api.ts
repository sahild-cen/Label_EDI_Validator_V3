const API_BASE_URL = 'http://localhost:8000';

export interface Carrier {
  _id: string;
  carrier: string;
  label_spec_path?: string;
  edi_spec_path?: string;
  has_label_rules?: boolean;
  has_edi_rules?: boolean;
  rules_version?: number | null;
}

export interface ValidationError {
  field: string;
  expected: string;
  actual: string;
  description: string;
}

export interface ValidationResult {
  status: string;
  errors: ValidationError[];
  corrected_label_script?: string;
  corrected_edi_script?: string;
  compliance_score: number;
}

export const api = {
  async uploadCarrierSpec(formData: FormData) {
    const response = await fetch(`${API_BASE_URL}/api/carriers/upload`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async listCarriers(): Promise<{ success: boolean; carriers: Carrier[] }> {
    const response = await fetch(`${API_BASE_URL}/api/carriers/list`);
    return response.json();
  },

  async getCarrier(carrierId: string) {
    const response = await fetch(`${API_BASE_URL}/api/carriers/${carrierId}`);
    return response.json();
  },

  async deleteCarrier(carrierId: string) {
    const response = await fetch(`${API_BASE_URL}/api/carriers/${carrierId}`, {
      method: 'DELETE',
    });
    return response.json();
  },

  async renameCarrier(carrierId: string, newName: string) {
    const response = await fetch(`${API_BASE_URL}/api/carriers/${carrierId}/rename`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ carrier_name: newName }),
    });
    return response.json();
  },

  async updateCarrierSpec(carrierId: string, formData: FormData) {
    const response = await fetch(`${API_BASE_URL}/api/carriers/${carrierId}/update-spec`, {
      method: 'PUT',
      body: formData,
    });
    return response.json();
  },

  async extractCarrierSpec(carrierCode: string, specFile: File, specType: 'label' | 'edi') {
    const formData = new FormData();
    formData.append('carrier_code', carrierCode);
    formData.append('spec_file', specFile);
    formData.append('spec_type', specType);
    const response = await fetch(`${API_BASE_URL}/api/carrier-setup/extract`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async validateLabel(carrierId: string, labelFile: File, isZpl: boolean, specName?: string) {
    const formData = new FormData();
    formData.append('carrier_id', carrierId);
    formData.append('label_file', labelFile);
    formData.append('is_zpl', isZpl.toString());
    if (specName) formData.append('spec_name', specName);

    const response = await fetch(`${API_BASE_URL}/api/validate/label`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async validateEDI(carrierId: string, ediFile: File) {
    const formData = new FormData();
    formData.append('carrier_id', carrierId);
    formData.append('edi_file', ediFile);

    const response = await fetch(`${API_BASE_URL}/api/validate/edi`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async getValidationHistory(carrierId: string, limit: number = 10) {
    const response = await fetch(
      `${API_BASE_URL}/api/validate/history/${carrierId}?limit=${limit}`
    );
    return response.json();
  },

  async detectSpec(labelFile: File) {
    const formData = new FormData();
    formData.append('label_file', labelFile);
    const response = await fetch(`${API_BASE_URL}/api/validate/detect-spec`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async detectEdiSpec(ediFile: File) {
    const formData = new FormData();
    formData.append('edi_file', ediFile);
    const response = await fetch(`${API_BASE_URL}/api/validate/detect-edi-spec`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  },

  async getSpecFiles(carrierCode: string, specType: 'label' | 'edi') {
    const response = await fetch(
      `${API_BASE_URL}/api/carrier-setup/spec-files/${encodeURIComponent(carrierCode)}?spec_type=${specType}`
    );
    return response.json();
  },

  async generateRules(carrierCode: string, specType: 'label' | 'edi', reviewedOnly: boolean = false) {
    const response = await fetch(
      `${API_BASE_URL}/api/carrier-setup/generate-rules/${encodeURIComponent(carrierCode)}?spec_type=${specType}&reviewed_only=${reviewedOnly}`,
      { method: 'POST' }
    );
    return response.json();
  },
};