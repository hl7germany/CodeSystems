import yaml, os, sys


def clamlconvert(claml):
  converter = claml["converter"]
  rv = 1
  for key, value in claml["clamlPackages"].items():
    print('converting: ' + key)
    rv = os.system('java dd-jar tools/' + converter + ' -i ' + value[
      "clamlfile"] + ' -designations ' + value["designations"] + ' -o generated-resources/' + value[
                "outputFolder"] + '/' + value["outputFileName"] + ' -id ' + key + ' -url ' + value[
                "url"] + ' -valueset ' + value["valueset"])
  return rv


with open('config.yaml') as config:
  returnValue = 0
  data = yaml.safe_load(config)

  # claml handling
  ret = clamlconvert(data["packages"]["claml"])
  if ret != 0:
    returnValue = ret

  sys.exit(returnValue)
