import sublime
import sublime_plugin


class QueryToJsStringCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
       for start_coordinate in self.getStartCoordinates(region):
          start_point = self.getStartPoint(start_coordinate)
          self.view.replace(edit, start_point, self.encloseString(self.view.substr(start_point)))

  def getStartCoordinates(self, region):
    """ Gets the starting column and row for each line in selection """
    return self.setAllColumnsToZero([self.view.rowcol(x.a) for x in self.view.split_by_newlines(region)])

  def encloseString(self, string):
    """ Helper function to wrap the string """
    open_closure = '"'
    end_closure = ' " +'
    return open_closure + string + end_closure

  def setAllColumnsToZero(self, coordinates):
    """ Sets the column coordinate to 0.  This enables wrapping without
    having to be at the start of the selection
    """
    return [(x[0], 0) for x in coordinates]

  def getStartPoint(self, coordinate):
    """ Returns the starting point of the string, skipping over white space """
    return self.view.find(r'\S.*\S', self.view.text_point(*coordinate))























