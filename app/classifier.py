class FeatureClassifier:

    def get_filename(self, row):

        feature_type = str(row["النوع"]).strip()
        description = str(row["descriptio"]).strip()

        if feature_type == "أرض":
            return "land"

        if feature_type == "مبني":

            text = description.replace(" ", "")

            if "3مبنى" in text:
                return "boundary"

            if "2مبنى" in text:
                return "boundary"

            if "4مبنى" in text:
                return "boundary"

            if "5مبنى" in text:
                return "boundary"

            return "build"

        return "feature"