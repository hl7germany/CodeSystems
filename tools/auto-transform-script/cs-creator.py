import yaml, os


def clamlconvert(claml):
  converter = claml["converter"]
  for key, value in claml["clamlPackages"].items():
    print('converting: ' + key)
    os.system('java -jar tools/' + converter + ' -i ' + value[
      "clamlfile"] + ' -designations ' + value["designations"] + ' -o generated-resources/' + value[
                "outputFolder"] + '/' + value["outputFileName"] + ' -id ' + key + ' -url ' + value[
                "url"] + ' -valueset ' + value["valueset"])


with open('config.yaml') as config:
  data = yaml.safe_load(config)

  # claml handling
  clamlconvert(data["packages"]["claml"])
