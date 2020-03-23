import yaml, os, sys


def clamlconvert(claml):
  retVal = 0
  converter = claml["converter"]
  for key, value in claml["clamlPackages"].items():
    print('converting: ' + key)
    print('java -jar tools/' + converter + ' -i ' + value[
                                                 "clamlfile"] + ' -designations ' + value["designations"] + ' -o generated-resources/' + value[
      "outputFolder"] + '/' + value["outputFileName"] + ' -id ' + key + ' -url ' + value[
                                                                "url"] + ' -valueset ' + value["valueset"])
    rv = os.system('java -jar tools/' + converter + ' -i ' + value[
      "clamlfile"] + ' -designations ' + value["designations"] + ' -o generated-resources/' + value[
                     "outputFolder"] + '/' + value["outputFileName"] + ' -id ' + key + ' -url ' + value[
                     "url"] + ' -valueset ' + value["valueset"])
    if rv != 0:
      retVal = rv
  return retVal


with open('config.yaml') as config:
  data = yaml.safe_load(config)

  # claml handling
  returnValue = clamlconvert(data["packages"]["claml"])
  sys.exit(returnValue)
