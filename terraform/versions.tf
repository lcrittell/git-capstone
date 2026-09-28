terraform {
  required_providers {
    vercel = {
      source  = "vercel/vercel"
      version = "~> 2.0"
    }
  }

  required_version = ">= 1.6.0"

  cloud {
    organization = "git_capstone"

    workspaces {
      name = "git-capstone"
    }
  }
}