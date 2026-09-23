import glob
import re

css_files = glob.glob('*.css')

ctct_remove_oval_rule = """
/* Remove Constant Contact inner oval shapes, borders and shadows from form wrappers */
.ctct-inline-form form,
.ctct-inline-form div,
.ctct-inline-form fieldset,
.ctct-embed-signup form,
.ctct-embed-signup div,
.ctct-embed-signup fieldset,
.ctct-form-embed,
.ctct-form-defaults,
.ctct-form-wrapper,
div[class*="ctct-form"],
form[class*="ctct-form"] {
  border-radius: 0 !important;
  box-shadow: none !important;
  background-color: transparent !important;
  background: transparent !important;
}

/* Explicitly preserve rounded corners for inputs and submit button */
.ctct-inline-form input[type="email"],
.ctct-embed-signup input[type="email"],
.ctct-inline-form input[type="text"],
.ctct-embed-signup input[type="text"],
.ctct-inline-form textarea,
.ctct-embed-signup textarea {
  border-radius: 8px !important;
}

.ctct-inline-form button[type="submit"],
.ctct-embed-signup button[type="submit"],
.ctct-inline-form .ctct-form-button,
.ctct-embed-signup .ctct-form-button,
.ctct-button {
  border-radius: 999px !important;
}
"""

updated_count = 0

for filepath in css_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove previous oval fix blocks if any to prevent clutter
        content = re.sub(r'/\* Remove Constant Contact inner oval shapes[\s\S]*?\n\}', '', content)
        content = re.sub(r'/\* Remove Constant Contact internal widget background[\s\S]*?\n\}', '', content)

        if 'ctct-inline-form' in content or 'ctct-embed-signup' in content or 'ctct' in content:
            content += "\n" + ctct_remove_oval_rule
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"Removed CTCT oval shape in: {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

print(f"\nTotal CSS files updated: {updated_count}")
