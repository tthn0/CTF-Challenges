import fs from "fs";
import path from "path";
import pino from "pino";
import { LOG_DIRECTORY_NAME, LOG_FILE_NAME } from "./environmentVariables.js";

const __dirname = import.meta.dirname;
const logDirectory = path.join(__dirname, "..", LOG_DIRECTORY_NAME);
const logFile = path.join(logDirectory, LOG_FILE_NAME);

fs.mkdirSync(logDirectory, { recursive: true });
const logStream = fs.createWriteStream(logFile, { flags: "a+" });
const logger = pino({ base: null, timestamp: false }, logStream);

const logRequest = (req, res, next) => {
  const date = new Date();
  const info = {
    date: date.toLocaleString("en-US"),
    ip: req.ip,
    userAgent: req.headers["user-agent"],
    method: req.method,
    path: req.originalUrl,
    body: req.body,
  };
  logger.info(info);
  console.log(info);
  next();
};

export { logRequest };
