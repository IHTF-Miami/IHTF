import glob
import re

css_files = glob.glob('*.css')

ctct_transparent_rule = """
/* Remove Constant Contact internal widget background, shadow, border and padding */
.ctct-inline-form .ctct-form-defaults,
.ctct-inline-form .ctct-form-wrapper,
.ctct-inline-form .ctct-form-embed,
.ctct-inline-form div[class*="ctct-form"],
.ctct-embed-signup .ctct-form-defaults,
.ctct-embed-signup .ctct-form-wrapper,
.ctct-embed-signup .ctct-form-embed,
.ctct-embed-signup div[class*="ctct-form"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}
"""

updated_count = 0

for filepath in css_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean existing inner box rule if present to avoid duplication
        content = re.sub(r'/\* Remove Constant Contact internal widget background[\s\S]*?\n\}', '', content)

        if 'ctct-inline-form' in content or 'ctct-embed-signup' in content or 'ctct' in content:
            content += "\n" + ctct_transparent_rule
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Applied transparent inner box CTCT rule in: {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

print(f"\nTotal CSS files updated: {updated_count}")
