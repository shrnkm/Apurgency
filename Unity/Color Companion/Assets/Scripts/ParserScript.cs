using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ParserScript : MonoBehaviour
{
    public InputField userIn;
    private string theInput;

    // the adjective dictionary
    private Dictionary<string, Tuple<int, int, int, int>> adjectives =
        new Dictionary<string, Tuple<int, int, int, int>>
        {
            {"red", new Tuple<int, int, int, int>(1, 0, 0, 0)},
            {"green", new Tuple<int, int, int, int>(0, 1, 0, 0)},
            {"blue", new Tuple<int, int, int, int>(0, 0, 1, 0)},
            {"yellow", new Tuple<int, int, int, int>(1, 1, 0, 0)},
            {"warm", new Tuple<int, int, int, int>(0, -1, 0, 0)},
            {"cold", new Tuple<int, int, int, int>(0, 0, 1, 0)},
            {"dark", new Tuple<int, int, int, int>(0, -1, -1, 0)},
            {"bright", new Tuple<int, int, int, int>(0, 1, 1, 0)},
            {"pale", new Tuple<int, int, int, int>(0, 0, 0, -1)},
            {"saturate", new Tuple<int, int, int, int>(0, 0, 0, 1)}
        };
    
    
    
    // list of adverbs for milli changes
    private static List<string> milli = new List<string> {"tiny", "bit", "slight", "little", "tad"};
    // list of adverbs for moderate changes
    private static List<string> moderate = new List<string> {"somehow", "somewhat", "moderately"};
    // list of adverbs for mega changes
    private static List<string> mega = new List<string> {"lot", "much", "big deal", "great deal", "very"};
    // create the dictionary of adverbs
    public Dictionary<int, List<string>> adverbs = new Dictionary<int, List<string>>
    {
        {1, milli}, {2, moderate}, {3, mega}
    };
    
    private void Start()
    {

    }


    public void OnSubmit()
    {

        theInput = userIn.text;
        Debug.Log("your input: " + theInput);

        var adverb = false;
        var adjective = false;

        var advVal = 1;
        var adjVal = new Tuple<int, int, int, int>(0, 0, 0, 0);

        
        // check the input for the adverb
        foreach(KeyValuePair<int, List<string>> entry in adverbs)
        {
            foreach (var adv in entry.Value)
            {
                if (theInput.Contains(adv))
                {
                    adverb = true;
                    advVal = entry.Key;
                    break;
                }
            }
            if (adverb) {break;}
        }
        Debug.Log("adverb value = " + advVal);

        // check the input for the adjective
        foreach (KeyValuePair<string, Tuple<int, int, int, int>> entry in adjectives)
        {
            if (theInput.Contains(entry.Key))
            {
                adjective = true;
                adjVal = entry.Value;
                break;
            }
        }
        Debug.Log("adverb value = " + adjVal);
    }
    
    void Update()
    {


    }
}
 