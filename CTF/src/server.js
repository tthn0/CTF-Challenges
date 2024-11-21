import express from "express";
import { Admin } from "./admin.js";
import { User } from "./user.js";
import { PORT } from "./environmentVariables.js";

const app = express();
app.use(express.json());

const logger = (req, res, next) => {
  const date = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    weekday: "short",
    month: "short",
    day: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(new Date());
  console.log(`${date}`);
  console.log(`\t${req.ip}`);
  console.log(`\t${req.method} ${req.originalUrl}`);
  console.log(`\t${JSON.stringify(req.body)}`);
  next();
};

app.use(logger);

app.get("/", (req, res) => {
  res.end("Please send a POST request to `/user` or `/admin`.");
});

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
