def link_requests(project):

    linked = 0

    missing = 0

    for date in project.date_folders:

        for request in date.requests:

            excel = project.excel_database.get(request.request_number)

            if excel:

                request.excel = excel
                linked += 1

            else:

                print(f"Excel record not found: {request.request_number}")

                missing += 1

    print("\n")
    print("=" * 50)
    print("Link Report")
    print("=" * 50)

    print(f"Linked : {linked}")

    print(f"Missing : {missing}")