import express from "express";
import { Admin } from "./admin.js";
import { PORT } from "./environmentVariables.js";
import { logRequest } from "./logRequest.js";
import { User } from "./user.js";

const app = express();
app.use(express.json());
app.use(logRequest);

app.post("/user", (req, res) => {
  const user = new User(req.body);
  res.end(user.message);
});

app.post("/admin", (req, res) => {
  const admin = new Admin(req.body);
  res.end(admin.message);
});

app.use((err, req, res, next) => {
  res.status(500).end("An internal server error occurred.");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
