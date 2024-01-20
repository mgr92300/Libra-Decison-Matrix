package LibraDecision;

import javax.swing.*;

public class Selectors
  {
    //Constants
    protected static boolean TooManyOptions()
      {
        System.out.println("Too Many Options");
        int NumOptionsAvailable, ChosenOption, OptIter;
        String NOAPrompt, OptionPrompt, Selection;
        NOAPrompt = "How many options are there available?";
        OptionPrompt = "State an option."
        NumOptionsAvailable = Integer.parseInt(getCondition(NOAPrompt));
        String[] ArrayOfOptions = new String[NumOptionsAvailable];
        for (OptIter = 0, OptIter < NumOptionsAvailable; OptIter++)
          {
            ArrayOfOptions[OptIter] = getCondition(OptionPrompt);
          }
        ChosenOption = getRandBetween(0, NumOptionsAvailable);
        Selection = ArrayOfOptions[ChosenOption];
        System.out.println("I've chosen" + Selectors);
        return true;
      }

	  protected static boolean FiftyFiftySplit()
      {
        System.out.println("Fifty Fifty");
        int ConditionIndex, ChosenCondition;
        String[] ArrayOfCondition = new String[2];
        for (ConditionIndex = 0; ConditionIndex < 2; ConditionIndex++)
          {
            ArrayOfCondition[ConditionIndex] = getCondition("State Condition");
          }
        ChosenCondition = getRandBetween(0,1);
        System.out.println("I have Chosen:" + ArrayOfCondition[ChosenCondition]);
        return true;
      }

    protected static boolean ToBeOrNotToBe()
      {
        if (YesNoDialog("Is this Voluntary","Checkpoint1"))
          {
            if (!YesNoDialog("Is outside influence involved?", "Checkpoint2"))
              {
                if (YesNoDialog("Will you accept either answer", "Checkpoint 3"))
                  {
                    return FiftyFiftySplit();
                  }
              }
          }
         return true;
      }

    protected static boolean ProsAndCons()
      {
        System.out.println("P's and C's");
        System.out.println("Currently being developed.");
        return true;
      }

    private static int getRandBetween( int lowLimit, int highLimit )
      {
        int range = highLimit - lowLimit + 1;
        return (int)( Math.random() * range );
      }

    public static String[] getOptions()
      {
        String[] selector = new String[4];
        //current selectors Too Many Options","Fifty Fifty Split","Should I or Shouldn't I?","Pro and Cons List"
      	for (int index = 0; index < 4; index++)
      		{
      		  if(index == 0)
            	selector[index] = "Too Many Options";
      		  else if (index == 1)
      				selector[index] = "Fifty Fifty Split";
      		  else if (index == 2)
      				selector[index] = "Should I or Shouldn't I?";
      		  else if (index == 3)
              selector[index] = "Pro and Cons List";
          }
        return selector;
      }

    public static boolean YesNoDialog(String Prompt, String Title)
      {
        int Option1 = JOptionPane.showConfirmDialog(null, Prompt, Title, JOptionPane.YES_NO_OPTION);
        return Option1 == JOptionPane.YES_OPTION; // if they pushed yes button, result is true
      }

    public static String getCondition(String Prompt)
      {
        String UserInputStr;
        UserInputStr = JOptionPane.showInputDialog(Prompt);
        return UserInputStr;
      }
  }


/*Creation of a new JOptionPane
		JOptionPane pane = new JOptionPane(selector);
	    //Configure pane settings
		pane.setMessageType(JOptionPane.PLAIN_MESSAGE);
		pane.setMessage("Choose a selector");
		pane.setOptionType(JOptionPane.DEFAULT_OPTION);
		pane.setOptions(selector);
	  JDialog dialog = pane.createDialog(null, "This is epic");
	  dialog.show();
*/
  public void recursionPane()
    {
    	JOptionPane pane = new JOptionPane(selector);
        //Configure pane settings
      pane.setMessageType(JOptionPane.PLAIN_MESSAGE);
      pane.setMessage("Choose a selector");
      pane.setOptionType(JOptionPane.DEFAULT_OPTION);
      pane.setOptions(selector);
      JDialog dialog = pane.createDialog(null, "");
      dialog.show();
    }
