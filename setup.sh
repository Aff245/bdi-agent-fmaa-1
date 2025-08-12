#!/bin/bash
echo "🚀 Initializing BDI Agent FMAA Environment..."

mkdir -p orchestrator termux edge security monitoring deployment

echo "✅ Folder structure created."
echo "📦 Installing additional tools..."

# Optional CLI tools
npm install -g supabase

echo "🎉 Setup complete. Ready to code!"
