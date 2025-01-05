job "tara-bot" {
  datacenters = ["dc1"]
  type = "service"

  group "python-bot" {
    count = 1

    restart {
      attempts = 3
      delay    = "30s"
    }

    task "tara-bot" {
      driver = "docker"

      config {
        image = "ghcr.io/alanreviews/discordpy-bot/tara-bot:latest"
      }

      resources {
        cpu    = 64
        memory = 64
      }

      template {
        data = <<EOH
DISCORD_TOKEN={{ with nomadVar "nomad/jobs/tara-bot" }}{{ .DISCORD_TOKEN }}{{ end }}
ENVIRONMENT=production
EOH

        destination = "secrets/file.env"
        env         = true
      }
    }
  }
}
