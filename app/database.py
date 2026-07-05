from app.models import ExcelRequest


def build_request_database(df):

    database = {}

    for _, row in df.iterrows():

        request = ExcelRequest(

            surv_num=str(row[0]).strip(),

            request_nu=str(row[1]).strip(),

            gov=str(row[2]),

            sec=str(row[3]),

            location=str(row[4]),

            area=float(row[5]),

            request_type=str(row[6]),

            request_date=str(row[7]),

            owner=str(row[8]),

            phone=str(row[9]),

            company=str(row[10]),

            survey_status=str(row[11]),

            geodesy_status=str(row[12]),

            inspection_status=str(row[13])

        )

        database[request.surv_num] = request

    return database