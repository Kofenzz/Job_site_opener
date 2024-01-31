import tkinter as tk
import webbrowser

class JobSiteOpener:
    def __init__(self, master):
        self.master = master
        master.title("Job Site Opener")

        self.job_sites = {
            "LinkedIn QA": "https://www.linkedin.com/jobs/search/?currentJobId=3804500044&distance=25&f_E=1%2C2%2C3&f_TPR=r604800&geoId=105773754&keywords=qa&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true",
            "LinkedIn Junior Java": "https://www.linkedin.com/jobs/search/?currentJobId=3804500044&f_E=1%2C2%2C3&f_TPR=r604800&geoId=105773754&keywords=junior%20java&location=Bucharest%2C%20Romania&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true",
            "Envada": "https://www.endava.com/careers/jobs",
            "Thales": "https://careers.thalesgroup.com/global/en/c/software-jobs",
            "EveryMatrix": "https://everymatrix.teamtailor.com/jobs?location=Bucharest&query=",
            "BlankFactor": "https://blankfactor.wd12.myworkdayjobs.com/Blankfactor_External?locations=893948fa336d1000cd5db9fd84360000&locations=893948fa336d1000cd34c9b0904c0000",
            "Accenture": "https://www.accenture.com/ro-en/careers/jobsearch?jk=&sb=1&vw=0&is_rj=0&pg=1&ct=bucharest&ba=technology&jt=entry-level%20job",
        }

        self.create_site_buttons()

    def create_site_buttons(self):
        row_num = 0
        for site, url in self.job_sites.items():
            button = tk.Button(self.master, text=site, command=lambda u=url: self.open_job_site(u))
            button.grid(row=row_num // 3, column=row_num % 3, padx=10, pady=10)
            row_num += 1

    def open_job_site(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = JobSiteOpener(root)
    root.mainloop()
