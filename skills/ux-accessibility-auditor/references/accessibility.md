# Accessibility checklist

Use WCAG 2.2 AA as a practical target and record what was manually and automatically checked.

Review:

- semantic landmarks, heading hierarchy, names, roles, and values;
- labels, instructions, required state, input purpose, validation, and error association;
- keyboard order, visible focus, skip links, menus, dialogs, popovers, and focus restoration;
- screen-reader announcements for status, errors, loading, and dynamic content;
- contrast, non-color cues, text resizing, zoom, motion preferences, and touch target behavior;
- meaningful alternative text and appropriate treatment of decorative imagery;
- tables, charts, media, time limits, authentication, and repeated components.

Do not add ARIA where native semantics solve the problem. Test with keyboard-only navigation and at least one available assistive technology when possible. Report unavailable manual checks as NOT_VERIFIED.
