import { Router } from "../deps.js";
import * as mainController from "./controllers/mainController.js";

const router = new Router();

router.get("/", mainController.showMain);
router.post("/",mainController.login)
router.get("/dash", mainController.dashboard);
router.get("/:name/status",mainController.Driver_status);
export { router };
