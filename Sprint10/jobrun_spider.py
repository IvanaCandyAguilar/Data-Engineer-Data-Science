import scrapy
import pandas as pd


class JobSpider(scrapy.Spider):
    name = "jobrun"
    start_urls = ["https://jobrun.dev/ofertas"]  # Reemplazar con la URL de la página a scrapear

    def parse(self, response):
        job_cards = response.css("div.__wab_flex-container div.plasmic_job_run_all__6OLuV.PlasmicOfferCard_freeBox___8Vji7__iE5Rg")
        
        for card in job_cards:
            empresa = card.css("div.__wab_slot-string-wrapper::text").get()
            puesto = card.css("div.plasmic_job_run_all__6OLuV.PlasmicOfferCard_freeBox__zEZtJ__h_k5H div.__wab_slot-string-wrapper::text").get()
            salario = card.css("div.plasmic_job_run_all__6OLuV.PlasmicOfferCard_freeBox__wq10V__axvOC div.__wab_slot-string-wrapper::text").get()
            lugar = card.css("div.plasmic_job_run_all__6OLuV.PlasmicOfferCardDetailsItem_svgtype_ciudad__FmyGa div.__wab_slot-string-wrapper::text").get()
            tiempo = card.css("div.plasmic_job_run_all__6OLuV.PlasmicOfferCardDetailsItem_svgtype_remote__hPyK9 div.__wab_slot-string-wrapper::text").get()
            
            yield {
                "Empresa": empresa,
                "Puesto": puesto,
                "Salario": salario,
                "Lugar": lugar,
                "Tiempo": tiempo
            }

        # Aquí puedes agregar la lógica para navegar a la siguiente página si es necesario


