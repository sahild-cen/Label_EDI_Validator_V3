"""
Test script for ^GF graphic decoder in zpl_parser.py
"""
import sys
import os

# Add parent to path so we can import app modules
sys.path.insert(0, os.path.dirname(__file__))

from app.services.zpl_parser import (
    _extract_gf_data_block,
    _decompress_zpl_gf,
    _hex_rows_to_image,
    _calc_pixel_density,
    _decode_all_gf_graphics,
    parse_zpl_to_raw,
)


def test_decompress_basic():
    """Test basic hex passthrough (no compression)."""
    rows = _decompress_zpl_gf("FF00FF00", bytes_per_row=2)
    assert len(rows) == 2, f"Expected 2 rows, got {len(rows)}"
    assert rows[0] == "FF00", f"Row 0: expected 'FF00', got '{rows[0]}'"
    assert rows[1] == "FF00", f"Row 1: expected 'FF00', got '{rows[1]}'"
    print("  PASS: basic hex passthrough")


def test_decompress_repeat_uppercase():
    """Test G-Y repeat (1-19 times)."""
    # H = repeat 2 times, so HF = FF
    rows = _decompress_zpl_gf("HF,", bytes_per_row=1)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0] == "FF", f"Expected 'FF', got '{rows[0]}'"
    print("  PASS: uppercase repeat (G-Y)")


def test_decompress_repeat_lowercase():
    """Test g-y repeat (multiples of 20)."""
    # g = 20 repeats of next char
    rows = _decompress_zpl_gf("g0,", bytes_per_row=10)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0] == "0" * 20, f"Expected 20 zeros, got '{rows[0]}'"
    print("  PASS: lowercase repeat (g-y)")


def test_decompress_additive():
    """Test g-y + G-Y additive repeat."""
    # gH0 = (20 + 2) * '0' = 22 zeros
    rows = _decompress_zpl_gf("gH0,", bytes_per_row=11)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0] == "0" * 22, f"Expected 22 zeros, got '{rows[0]}'"
    print("  PASS: additive repeat (g + G)")


def test_decompress_colon():
    """Test colon = repeat previous row."""
    # First row FF00, then colon repeats it
    rows = _decompress_zpl_gf("FF00:", bytes_per_row=2)
    assert len(rows) == 2, f"Expected 2 rows, got {len(rows)}"
    assert rows[0] == "FF00", f"Row 0: '{rows[0]}'"
    assert rows[1] == "FF00", f"Row 1: '{rows[1]}'"
    print("  PASS: colon (repeat previous row)")


def test_decompress_comma():
    """Test comma = fill rest with 0."""
    rows = _decompress_zpl_gf("FF,", bytes_per_row=4)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0] == "FF000000", f"Expected 'FF000000', got '{rows[0]}'"
    print("  PASS: comma (fill with 0)")


def test_decompress_bang():
    """Test bang = fill rest with F."""
    rows = _decompress_zpl_gf("00!", bytes_per_row=4)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0] == "00FFFFFF", f"Expected '00FFFFFF', got '{rows[0]}'"
    print("  PASS: bang (fill with F)")


def test_image_creation():
    """Test PIL Image creation from hex rows."""
    # 1 byte per row = 8 pixels wide, 2 rows
    rows = ["FF", "00"]
    img = _hex_rows_to_image(rows, bytes_per_row=1)
    if img is None:
        print("  SKIP: PIL not available")
        return
    assert img.size == (8, 2), f"Expected (8,2), got {img.size}"
    density = _calc_pixel_density(img)
    assert 0.4 < density < 0.6, f"Expected ~0.5 density, got {density}"
    print(f"  PASS: PIL Image created ({img.size}, density={density})")


def test_real_label():
    """Test against a real ZPL label with ^GFA graphics."""
    label_path = os.path.join(
        os.path.dirname(__file__),
        "uploads",
        "labels_dbace894-c8f0-476e-b596-d602d2c1fa0b.zpl",
    )
    if not os.path.exists(label_path):
        print("  SKIP: test label file not found")
        return

    script = open(label_path, "r", encoding="utf-8", errors="ignore").read()
    print(f"  Label size: {len(script):,} chars")

    # Test full parser
    raw = parse_zpl_to_raw(script)

    print(f"  Text blocks: {len(raw['text_blocks'])}")
    print(f"  Barcodes:    {len(raw['barcodes'])}")
    print(f"  Graphics:    {len(raw['graphics'])}")
    print(f"  ZPL commands: {raw['zpl_commands']}")

    for i, g in enumerate(raw["graphics"]):
        has_img = "PIL Image" if g.get("image") else "NO IMAGE"
        print(
            f"    Graphic {i}: type={g['type']}  pos=({g['x']},{g['y']})  "
            f"size={g['width']}x{g['height']}  "
            f"density={g['pixel_density']:.1%}  [{has_img}]"
        )

    assert len(raw["graphics"]) > 0, "Expected at least one graphic"
    for g in raw["graphics"]:
        assert g["width"] > 0, f"Graphic has 0 width"
        assert g["height"] > 0, f"Graphic has 0 height"
        if g.get("image"):
            assert g["pixel_density"] >= 0, "Bad pixel density"

    # Check text blocks have font_cmd
    for tb in raw["text_blocks"][:3]:
        print(f"    Text: ({tb['x']},{tb['y']}) font={tb.get('font_cmd','')} '{tb['text'][:40]}'")

    print("  PASS: real label parsed with graphics decoded")


if __name__ == "__main__":
    print("=" * 60)
    print("ZPL ^GF Graphic Decoder Tests")
    print("=" * 60)

    print("\n1. Decompression unit tests:")
    test_decompress_basic()
    test_decompress_repeat_uppercase()
    test_decompress_repeat_lowercase()
    test_decompress_additive()
    test_decompress_colon()
    test_decompress_comma()
    test_decompress_bang()

    print("\n2. PIL Image creation:")
    test_image_creation()

    print("\n3. Real label test:")
    test_real_label()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)
