import crypto from "crypto";
import { User } from "./user.js";

class Admin extends User {
  // This is the hash of something super secret
  #SECRET_HASH = "0e017509330106083103990269772661";

  constructor(attributes) {
    // Call the `User` constructor
    super(attributes);

    // Check if a password was provided (`this.password` will be null if tampering was detected)
    if (!this.password) {
      this.message = "You shall not pass.";
      return;
    }

    // Hash the provided password
    const hash = crypto.createHash("md5").update(this.password).digest("hex");

    // Compare the hashes
    if (hash == this.#SECRET_HASH) {
      this.isAdmin = true;
    }

    // Update the message based on the provided password
    if (this.isAdmin) {
      this.message = `Welcome, admin. The flag is: ${this.flag}.`;
    } else {
      this.message = "You are not an admin. Try the `/user` route instead.";
    }
  }
}

export { Admin };
