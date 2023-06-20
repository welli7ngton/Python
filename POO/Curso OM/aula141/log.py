# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self,msg):
        raise NotImplementedError("Implemente o método log")

    def log_error(self,msg):
        return self._log(f"Error: {msg}")

    def log_success(self,msg):
        return self._log(f"Success: {msg}")

class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada  = f"{msg} ({self.__class__.__name__})"
        print("salvando no log...", msg_formatada)
        with open(LOG_FILE, "a") as arq:
            arq.write(msg_formatada)
            arq.write("\n")

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f"{msg} ({self.__class__.__name__})") 


if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("erro")
    lp.log_success("sucesso")
    lf = LogFileMixin()
    lf.log_error("erro")
    lf.log_success("sucesso")
