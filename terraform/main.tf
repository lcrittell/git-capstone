provider "vercel" {
  api_token = var.vercel_api_token
}

resource "vercel_project" "git_capstone" {
  name = "git-capstone"

  root_directory = "frontend"

  build_command = "node generate-config.js"

  output_directory = "."

  git_repository = {
    type              = "github"
    repo              = "lcrittell/git-capstone"
    production_branch = "main"
  }

  lifecycle {
    ignore_changes = [
      enable_affected_projects_deployments,
      ignore_command,
      oidc_token_config,
      protection_bypass_for_automation_secret,
      team_id,
      vercel_authentication
    ]
  }
}

