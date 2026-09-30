provider "vercel" {
  api_token = var.vercel_api_token
}

provider "render" {
  api_key = var.render_api_token
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

resource "render_web_service" "staging_api" {
  name           = "mtg-pack-return-staging-api"
  plan           = "free"
  region         = "oregon"
  root_directory = "backend/"
  environment_id = "evm-daqn98ff3r2c73bf512g"
  start_command  = "uvicorn src.main:app --host 0.0.0.0 --port $PORT"

  runtime_source = {
    native_runtime = {
      auto_deploy = true
      branch      = "develop"

      build_command = "pip install -r requirements.txt"

      repo_url = "https://github.com/lcrittell/git-capstone"

      runtime = "python"
    }
  }
}

resource "render_web_service" "production_api" {
  name           = "mtg-pack-return-prod-api"
  plan           = "free"
  region         = "oregon"
  root_directory = "backend/"
  environment_id = "evm-daqn98ff3r2c73bf512g"

  start_command = "uvicorn src.main:app --host 0.0.0.0 --port $PORT"
  runtime_source = {
    native_runtime = {
      auto_deploy = true
      branch      = "main"

      build_command = "pip install -r requirements.txt"

      repo_url = "https://github.com/lcrittell/git-capstone"

      runtime = "python"
    }
  }
}

