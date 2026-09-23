import glob
import re

css_files = glob.glob('*.css')

ctct_strict_hide = """
/* Explicitly hide CTCT success & error containers (supporting both style="display:none;" and style="display: none;") */
.ctct-inline-form #success_message_0,
.ctct-inline-form #error_message_0,
.ctct-inline-form #network_error_message_0,
.ctct-inline-form .ctct-form-success,
.ctct-inline-form .ctct-form-error,
.ctct-embed-signup #success_message_0,
.ctct-embed-signup #error_message_0,
.ctct-embed-signup #network_error_message_0,
.ctct-embed-signup .ctct-form-success,
.ctct-embed-signup .ctct-form-error {
  display: none !important;
}

/* Only show success message upon active success state */
.ctct-inline-form.ctct-state-success #success_message_0,
.ctct-inline-form .ctct-form-wrapper.ctct-state-success #success_message_0,
.ctct-inline-form.ctct-state-success .ctct-form-success,
.ctct-inline-form .ctct-form-wrapper.ctct-state-success .ctct-form-success,
.ctct-embed-signup.ctct-state-success #success_message_0,
.ctct-embed-signup .ctct-form-wrapper.ctct-state-success #success_message_0 {
  display: block !important;
}

/* Only show error message upon active error state */
.ctct-inline-form.ctct-state-error #error_message_0,
.ctct-inline-form.ctct-state-error #network_error_message_0,
.ctct-inline-form .ctct-form-wrapper.ctct-state-error #error_message_0,
.ctct-inline-form .ctct-form-wrapper.ctct-state-error #network_error_message_0,
.ctct-embed-signup.ctct-state-error #error_message_0 {
  display: block !important;
}
"""

updated_count = 0

for filepath in css_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix spacing attribute selector mismatch
        new_content = content.replace(':not([style*="display: none"])', ':not([style*="display: none"]):not([style*="display:none"])')

        # Clean existing CTCT hide blocks if present
        new_content = re.sub(r'/\* Explicitly hide CTCT success[\s\S]*?\n\}', '', new_content)
        new_content = re.sub(r'/\* Respect Constant Contact native visibility[\s\S]*?\n\}', '', new_content)

        # Append strict CTCT hide rule to files containing CTCT rules
        if 'ctct-inline-form' in new_content or 'ctct-embed-signup' in new_content or 'ctct' in new_content:
            new_content += "\n" + ctct_strict_hide

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        updated_count += 1
        print(f"Fixed CTCT CSS in: {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"\nTotal CSS files updated: {updated_count}")
