package LibraDecision;

import javax.swing.*;

public class LibraDecisionMatrix
{
  public static void main(String[] args)
	{
      String[] selectors = new String[4];
      boolean completedSelector = false;
      do
        {
          selectors = Selectors.getOptions();
          //New pane
          JOptionPane pane = new JOptionPane(selectors);
      	  //Configure pane settings
      		pane.setMessageType(JOptionPane.PLAIN_MESSAGE);
      		pane.setMessage("Choose a selector");
      		pane.setOptionType(JOptionPane.DEFAULT_OPTION);
      		pane.setOptions(selectors);

          JDialog dialog = pane.createDialog(null, "Libra Decision Matrix");
      	  dialog.show();

          Object selectedSelector = pane.getValue();
          completedSelector = getDecision(selectedSelector);
        }
      while (!completedSelector);
      fin();
	}

  private static boolean getDecision(Object selectedValue)
    {
      if(selectedValue == "Too Many Options")
  		  return Selectors.TooManyOptions();
      else if(selectedValue == "Fifty Fifty Split")
  		  return Selectors.FiftyFiftySplit();
  	  else if (selectedValue == "Should I or Shouldn't I?")
  		  return Selectors.ToBeOrNotToBe();
  	  else if (selectedValue == "Pro and Cons List")
  		  return Selectors.ProsAndCons();
  	  else
  		  return true;
    }

  private static void fin()
    {
	    System.out.println("Completed");
    }

}
