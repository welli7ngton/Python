from log import LogPrintMixin,LogFileMixin

lp = LogPrintMixin()
lp.log_error("erro")
lp.log_success("sucesso")
lf = LogFileMixin()
lf.log_error("erro")
lf.log_success("sucesso")