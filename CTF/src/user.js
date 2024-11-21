import { FLAG, PASSWORD } from "./environmentVariables.js";

class User {
  constructor(attributes) {
    // Don't allow the `isAdmin` attribute to be tampered with
    if (attributes.isAdmin) {
      this.message = "Nice try, buddy.";
      return;
    }

    // If `attributes` contains a `flag` key, then the user is requesting the flag
    if (attributes.flag) {
      this.flag = FLAG;
    }

    // For non-admins, set instance attributes
    for (const key in attributes) {
      if (new.target === User || !this.isAdmin) {
        this[key] = attributes[key];
      }
    }

    // Update the message based on the provided password
    if (this.password === PASSWORD) {
      this.isAdmin = true;
      this.message = "You're an admin. Try the `/admin` route instead.";
    } else {
      this.message = `Welcome, user. The flag is: ${this.flag}`;
    }
  }
}

export { User };
