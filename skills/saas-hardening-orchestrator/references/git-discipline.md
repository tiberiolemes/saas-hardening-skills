# Orchestrator Git procedure

Run the following read-only preflight from the application repository:

~~~bash
git status --short --branch
git remote -v
git branch --show-current
git log -5 --oneline
~~~

Record the full current commit SHA and the list of pre-existing changes in the checkpoint. If the tree is dirty, preserve those paths and do not stage them by broad globbing.

A stage commit may contain only the stage report, status update, authorized fixes, and tests that belong to that stage. Review the path list, diff, and secret scan immediately before committing. Prefer a dedicated branch only when switching is safe and authorized.

Do not use reset --hard, clean -fd, force push, broad checkout/discard, or destructive data commands. A gate passing never authorizes a push. Push only after the user explicitly asks for it and the remote, branch, diff, and secret review are current.
