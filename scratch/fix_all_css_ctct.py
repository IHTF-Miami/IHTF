import glob
import re

css_files = glob.glob('*.css')

ctct_hide_rule = """
/* Respect Constant Contact native visibility for success and error messages */
.ctct-inline-form .ctct-form-success,
.ctct-inline-form .ctct-form-error,
.ctct-inline-form [class*="ctct-form-success"]:not(.ctct-state-success),
.ctct-inline-form [class*="ctct-form-error"]:not(.ctct-state-error),
.ctct-inline-form [class*="success-message"]:not(.active),
.ctct-inline-form [class*="error-message"]:not(.active),
.ctct-inline-form h2[class*="success"],
.ctct-inline-form h3[class*="success"],
.ctct-inline-form div[class*="success"]:not(.ctct-state-success),
.ctct-embed-signup .ctct-form-success,
.ctct-embed-signup .ctct-form-error,
.ctct-embed-signup [class*="ctct-form-success"]:not(.ctct-state-success),
.ctct-embed-signup [class*="ctct-form-error"]:not(.ctct-state-error) {
  display: none !important;
}

.ctct-inline-form.ctct-state-success .ctct-form-success,
.ctct-inline-form .ctct-form-wrapper.ctct-state-success .ctct-form-success,
.ctct-inline-form .ctct-form-success.ctct-state-success,
.ctct-embed-signup.ctct-state-success .ctct-form-success,
.ctct-embed-signup .ctct-form-wrapper.ctct-state-success .ctct-form-success {
  display: block !important;
}

.ctct-inline-form.ctct-state-error .ctct-form-error,
.ctct-inline-form .ctct-form-wrapper.ctct-state-error .ctct-form-error,
.ctct-embed-signup.ctct-state-error .ctct-form-error,
.ctct-embed-signup .ctct-form-wrapper.ctct-state-error .ctct-form-error {
  display: block !important;
}
"""

updated_count = 0

for filepath in css_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean existing partial CTCT hide blocks if any
        content = re.sub(r'/\* Respect Constant Contact native visibility[\s\S]*?\n\}', '', content)

        # Update generic paragraph & header rules if present
        content = content.replace('.ctct-inline-form p,', '.ctct-inline-form p:not([class*="success"]):not([class*="error"]),')
        content = content.replace('.ctct-embed-signup p,', '.ctct-embed-signup p:not([class*="success"]):not([class*="error"]),')

        # Append hide rule if file contains CTCT selectors
        if 'ctct-inline-form' in content or 'ctct-embed-signup' in content or 'ctct' in content:
            content += "\n" + ctct_hide_rule

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        updated_count += 1
        print(f"Updated CTCT CSS in: {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

print(f"\nTotal CSS files updated: {updated_count}")
