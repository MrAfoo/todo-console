# Spec-Kit-Plus Plugin Integration

## Installation Date
$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Source
- **Repository**: ./spec-kit-plus
- **Version**: Based on spec-kit-plus local copy

## Components Installed

### 1. Templates (`.specify/templates/`)
- `adr-template.md` - Architecture Decision Record template
- `agent-file-template.md` - Agent configuration template
- `checklist-template.md` - Quality checklist template
- `phr-template.prompt.md` - Prompt History Record template
- `plan-template.md` - Planning document template
- `spec-template.md` - Specification template
- `tasks-template.md` - Task breakdown template
- `vscode-settings.json` - VS Code configuration

### 2. Memory Files (`.specify/memory/`)
- `command-rules.md` - Command execution rules
- `constitution.md` - Project constitution
- `constitutionplus.md` - Enhanced constitution

### 3. Slash Commands (`.claude/commands/`)
All spec-kit-plus commands prefixed with `sp.`:
- `/sp.adr` - Create Architecture Decision Record
- `/sp.analyze` - Analyze code or documentation
- `/sp.checklist` - Generate quality checklist
- `/sp.clarify` - Clarify requirements
- `/sp.constitution` - View/update project constitution
- `/sp.git.commit_pr` - Git commit and PR workflow
- `/sp.implement` - Implementation workflow
- `/sp.phr` - Create Prompt History Record
- `/sp.plan` - Create implementation plan
- `/sp.reverse-engineer` - Reverse engineer documentation
- `/sp.specify` - Create specification
- `/sp.tasks` - Break down into tasks
- `/sp.taskstoissues` - Convert tasks to issues

### 4. Scripts

#### Bash Scripts (`.specify/scripts/bash/`)
- `check-prerequisites.sh` - Verify required tools
- `common.sh` - Shared utility functions
- `create-adr.sh` - ADR creation script
- `create-new-feature.sh` - Feature scaffolding
- `create-phr.sh` - PHR creation script
- `setup-plan.sh` - Planning setup
- `update-agent-context.sh` - Update agent context

#### PowerShell Scripts (`.specify/scripts/powershell/`)
- `check-prerequisites.ps1` - Verify required tools
- `common.ps1` - Shared utility functions
- `create-new-feature.ps1` - Feature scaffolding
- `setup-plan.ps1` - Planning setup
- `update-agent-context.ps1` - Update agent context

## Usage

### In Claude Code
Use any slash command with the `sp.` prefix:
```
/sp.phr "Create user authentication feature"
/sp.spec "Add OAuth2 support"
/sp.plan "Implement caching layer"
```

### Via Scripts (PowerShell)
```powershell
.\.specify\scripts\powershell\create-phr.ps1 --title "My feature" --stage spec
.\.specify\scripts\powershell\setup-plan.ps1 --feature "my-feature"
```

### Via Scripts (Bash)
```bash
./.specify/scripts/bash/create-phr.sh --title "My feature" --stage spec
./.specify/scripts/bash/setup-plan.sh --feature "my-feature"
```

## Documentation
For full documentation, see:
- `spec-kit-plus/README.md` - Main documentation
- `spec-kit-plus/docs-plus/` - Extended documentation
- `spec-kit-plus/spec-driven.md` - Spec-driven methodology

## Updates
To update the plugin, run:
```powershell
# Copy latest templates
Copy-Item "spec-kit-plus/templates/*" ".specify/templates/" -Force -Recurse

# Copy latest scripts
Copy-Item "spec-kit-plus/scripts/*" ".specify/scripts/" -Force -Recurse

# Copy latest memory files
Copy-Item "spec-kit-plus/memory/*" ".specify/memory/" -Force
```
