import dotenv from "dotenv";
import path from "path";

if (process.env.NODE_ENV !== "production") {
  const __dirname = import.meta.dirname;
  const envPath = path.join(__dirname, "..", ".env.development");
  dotenv.config({ path: envPath });
}

const requiredVariables = [
  "LOG_FILE_NAME",
  "LOG_DIRECTORY_NAME",
  "PORT",
  "FLAG",
  "PASSWORD",
];
const missingVariables = requiredVariables.filter((v) => !process.env[v]);

if (missingVariables.length > 0) {
  throw new Error(
    `Missing required environment variables: ${missingVariables.join(", ")}`
  );
}

const PORT = process.env.PORT;
const FLAG = process.env.FLAG;
const PASSWORD = process.env.PASSWORD;
const LOG_FILE_NAME = process.env.LOG_FILE_NAME;
const LOG_DIRECTORY_NAME = process.env.LOG_DIRECTORY_NAME;

export { FLAG, LOG_DIRECTORY_NAME, LOG_FILE_NAME, PASSWORD, PORT };
