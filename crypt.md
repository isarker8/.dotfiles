# Managing Encrypted Files (git-crypt)

This repo uses [git-crypt](https://github.com/AGWA/git-crypt) to transparently encrypt selected files. Files are encrypted in the repository (and on GitHub) but appear as normal plaintext in the working directory when the repo is **unlocked**.

Which files are encrypted is controlled by the **`.gitattributes`** file in the repo root.

---

## Quick reference

| Task | Command |
|------|---------|
| Unlock the repo (decrypt) | `git-crypt unlock /path/to/dotfiles.key` |
| Lock the repo (re-encrypt working copy) | `git-crypt lock` |
| Show encryption status of all files | `git-crypt status` |
| Show only encrypted files | `git-crypt status -e` |
| Show only unencrypted files | `git-crypt status -u` |
| Check if a file matches an encryption rule | `git check-attr filter -- path/to/file` |
| Fix files that should be encrypted but aren't | `git-crypt status -f` |
| Export the key (for backup/sharing) | `git-crypt export-key /path/to/dotfiles.key` |

---

## How it works

A line in `.gitattributes` tells git-crypt which files to encrypt:

```gitattributes
secrets.env filter=git-crypt diff=git-crypt
config/*.json filter=git-crypt diff=git-crypt
secrets/** filter=git-crypt diff=git-crypt
```

Any file matching a pattern with `filter=git-crypt diff=git-crypt` is encrypted when committed.

> **Important:** `.gitattributes` itself must **never** be encrypted. If you use broad patterns (like `**`), add an exclusion:
>
> ```gitattributes
> .gitattributes !filter !diff
> ```

---

## Adding files to encryption

**Before you start:** make sure the repo is unlocked (`git-crypt status` should list your files, and they should be readable in plaintext).

### 1. Add a pattern to `.gitattributes`

```gitattributes
# single file
.config/app/config.toml filter=git-crypt diff=git-crypt

# all files in a folder
secrets/** filter=git-crypt diff=git-crypt

# by extension
*.pem filter=git-crypt diff=git-crypt
```

### 2. Commit `.gitattributes` **first**

```bash
git add .gitattributes
git commit -m "Encrypt config.toml with git-crypt"
```

Committing the rule before the file ensures the file is never committed in plaintext by accident.

### 3. Add the file(s)

**For a brand-new file:**

```bash
git add .config/app/config.toml
git commit -m "Add encrypted config"
```

**For a file that is already tracked in plaintext:**

```bash
git-crypt status -f          # re-stages files that should be encrypted
# or, alternatively:
git add --renormalize .

git commit -m "Encrypt existing config.toml"
```

### 4. Verify

```bash
git-crypt status -e
```

Your file should be listed as `encrypted`. You can also confirm with:

```bash
git check-attr filter -- .config/app/config.toml
# .config/app/config.toml: filter: git-crypt
```

> ⚠️ **Warning:** Encrypting an already-committed file only protects *future* commits. The plaintext remains in git history. If it contained real secrets (passwords, API keys, tokens, coordinates you'd rather keep private), **rotate them** where possible, and consider rewriting history with [`git filter-repo`](https://github.com/newren/git-filter-repo) or [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).

---

## Removing files from encryption

**Before you start:** the repo **must be unlocked**. If it is locked, git would commit the encrypted blob as if it were the plaintext file's content, corrupting it.

```bash
git-crypt unlock /path/to/dotfiles.key
```

### 1. Update `.gitattributes`

Either **delete** the matching line:

```diff
- .config/app/config.toml filter=git-crypt diff=git-crypt
```

Or, if the file matches a broader pattern you want to keep, add an **exclusion** *after* it (last match wins):

```gitattributes
secrets/** filter=git-crypt diff=git-crypt
secrets/public-notes.txt !filter !diff
```

### 2. Re-stage the file so git stores it as plaintext

```bash
git add .gitattributes
git add --renormalize .
# or for a specific file:
git rm --cached .config/app/config.toml && git add .config/app/config.toml
```

### 3. Commit

```bash
git commit -m "Stop encrypting config.toml"
```

### 4. Verify

```bash
git-crypt status -u
```

The file should now be listed as `not encrypted`.

> ⚠️ **Warning:** Older commits still contain the *encrypted* version of the file. Anyone who holds the git-crypt key can decrypt those historical versions.

---

## Common gotchas

- **File shows as binary garbage on GitHub.** This is expected. GitHub only sees the encrypted blob. Unlock locally to view it in plaintext.
- **File was committed unencrypted by mistake.** Run `git-crypt status -f`, commit, and rotate any secrets. History still contains the plaintext (see warnings above).
- **Pattern isn't matching.** Check with `git check-attr filter -- path/to/file`. Patterns follow `.gitignore`-style globbing, and later lines override earlier ones.
- **Changes to `.gitattributes` don't affect already-staged files.** Re-stage them with `git add --renormalize .`.
- **Fresh clone shows encrypted files.** You need to unlock it: `git-crypt unlock /path/to/dotfiles.key`.
- **Stow and encrypted files.** `stow .` symlinks the files as they are in the working tree, so unlock *before* stowing if you want the decrypted configs in place. Stowing a locked repo links the encrypted blobs, which the apps can't read.

---

## Key management

- **Never commit the key file** to the repository. If it lives near the repo, add it to `.gitignore`.
- Back up the key somewhere safe (e.g. a password manager). If it is lost, the encrypted files **cannot be recovered**.
- To share access with others, either share the exported key securely, or use GPG:
  ```bash
  git-crypt add-gpg-user USER_ID_OR_FINGERPRINT
  ```
