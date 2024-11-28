# 🚩 web-0x00

- **Difficulty**: `⭑⭑⭒⭒⭒⭒`
- **Language(s)**: `JavaScript`
- **Deployed Port**: `3000`
- **Deployed IP Address**:
  - Since I may occasionally switch between different hosting providers, the IP address will likely change every once in a while. The deployed IP address can be found in the **About** section on the GitHub sidebar and will be updated every time to reflect the current IP address.

## 🌀 Description

Something seems off with the account authentication system. Non-admin users are reporting strange messages, and the admin dashboard remains locked. Can you investigate the odd behavior and retrieve the hidden flag without triggering the system’s safeguards?

## 🌐 Hosting

> [!NOTE]
>
> - A docker installation is required to run this challenge.
> - Additionally, `sudo` might be required to run the commands if you're on Linux.

Create a clone of this branch and `cd` into the project directory. Follow the commands below to start the application, depending on how you want to run it.

### 🛠️ Development

```bash
cd CTF
sh start.sh 1
```

### 🚀 Production

> [!IMPORTANT]
> Follow these steps before starting:
>
> 1. Duplicate `CTF/.env.development`.
> 2. Rename the duplicate to `.env.production`.
> 3. Update the environment variables appropriately.

```bash
cd CTF
sh start.sh 2
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
