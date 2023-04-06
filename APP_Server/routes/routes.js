import { Router } from "../deps.js";
import * as mainController from "./controllers/mainController.js";

const router = new Router();

router.get("/", mainController.showMain);
router.post("/",mainController.login)
router.get("/dash", mainController.dashboard);
export { router };
