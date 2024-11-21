# 🚩 web-0x00

- **Difficulty**: `⭑⭑⭒⭒⭒⭒`
- **Language(s)**: `JavaScript`
- **Deployed Port**: `3000`
- **Deployed IP Address**:
  - Since I may occasionally switch between different hosting providers, the IP address will likely change every once in a while. The deployed IP address can be found in the **About** section on the GitHub sidebar and will be updated every time to reflect the current IP address.

## 🌀 Description

Something seems off with the account authentication system. Non-admin users are reporting strange messages, and the admin dashboard remains locked. Can you investigate the odd behavior and retrieve the hidden flag without triggering the system’s safeguards?

## 🌐 Hosting and Deployment

Create a clone of this branch and `cd` into the project directory. Follow the commands below to start the application, depending on how you want to run it.

### 💻 Development (No Docker)

Ideal for local development without Docker.

```bash
cd CTF
sh start.sh 1
```

### 🐳 Development (Docker)

Ideal for local development with Docker.

```bash
cd CTF
sh start.sh 2
```

### 🚀 Production

This is how the live application will be deployed.

> [!IMPORTANT]
> Follow these steps before starting:
>
> 1. Duplicate `CTF/.env.development`.
> 2. Rename the duplicate to `CTF/.env.production`.
> 3. Update the environment variables in `CTF/.env.production` appropriately.

```bash
cd CTF
sh start.sh 3
```

<section>
  <h2>💭 Hints</h2>
  <details>
    <summary>
      <strong>Hint 1</strong>
    </summary>
    Follow the chain of command, and you may find what you're looking for.
  </details>
  <details>
    <summary>
      <strong>Hint 2</strong>
    </summary>
    Inherited traits can be a blessing... or a vulnerability.
  </details>
  <details>
    <summary>
      <strong>Hint 3</strong>
    </summary>
    A little pollution in the right place can have big consequences.
  </details>
  <details>
    <summary>
      <strong>Hint 4</strong>
    </summary>
    Prototype pollution in JavaScript can lead to something unexpected.
  </details>
</section>
