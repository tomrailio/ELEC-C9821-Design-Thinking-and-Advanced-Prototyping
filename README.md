# ELEC-C9821-Design-Thinking-and-Advanced-Prototyping
To run the web application make sure to install Deno on your machine.
Using Shell (macOS and Linux):
    curl -fsSL https://deno.land/x/install/install.sh | sh
Using PowerShell (Windows):
    irm https://deno.land/install.ps1 | iex
Using Scoop (Windows):
    scoop install deno
Using Chocolatey (Windows):
    choco install deno
Using Homebrew (macOS):
    brew install deno
Using MacPorts (macOS): 
    sudo port install deno
Using Nix (macOS and Linux):
    nix-shell -p deno
Build and install from source using Cargo:
    cargo install deno --locked

After downloading Deno, make sure to have a running PostgreSQL database or a equivalent one, and change the credentials in database.js to your own database credentials.
connectionPool = new Pool({
  host: "Your database's host address",
  user: "Your database user",
  database: "Your database name",
  password: "Your database passsword",
  }, CONCURRENT_CONNECTIONS);

After finishing the above steps in terminal, go to the location where app-launch.js are, and run the command:
    deno run --allow-read --allow-write --allow-env --allow-net --unstable app-launch.js
And the application should start running on your localhost at port 7777.