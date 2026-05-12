#!/usr/bin/env bash
set -euo pipefail

echo "[install] legacy compatibility path for tracking-query"
echo "[install] prefer SkillHub CLI built-in Python installer for normal installs"

RUNTIME_ROOT="./.skillhub/runtime"
SITE_PACKAGES="${RUNTIME_ROOT}/site-packages"
BIN_DIR="./.skillhub/bin"

mkdir -p "${SITE_PACKAGES}" "${BIN_DIR}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is not installed"
    exit 1
fi

if ! python3 -m pip install --no-build-isolation --target "${SITE_PACKAGES}" .; then
    echo "[install] full dependency install failed, retrying package-only install"
    python3 -m pip install --no-build-isolation --no-deps --target "${SITE_PACKAGES}" .
fi

cat > "${BIN_DIR}/tracking-query" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUNTIME_DIR="${SCRIPT_DIR}/../runtime"
export PYTHONPATH="${RUNTIME_DIR}/site-packages:${PYTHONPATH:-}"
exec python3 -m tracking_query.skillhub_entry "$@"
EOF

chmod +x "${BIN_DIR}/tracking-query"
"${BIN_DIR}/tracking-query" --help >/dev/null
