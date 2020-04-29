using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class ParserScript : MonoBehaviour
{
    public InputField userIn;
    public static Color state;
    public Image stateImage;
    private string theInput;
    public TextMeshProUGUI Distance;
    private float distance = 0;
    

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
    
    
    
    // list of adverbs for minor changes
    private static List<string> minor = new List<string> {"tiny", "bit", "slight", "little", "tad"};
    // list of adverbs for moderate changes
    private static List<string> moderate = new List<string> {"somehow", "somewhat", "moderately"};
    // list of adverbs for major changes
    private static List<string> major = new List<string> {"lot", "much", "big deal", "great deal", "very"};
    // list of adverbs for negative changes
    private static List<string> negative = new List<string> {"less"};
    // create the dictionary of adverbs
    public Dictionary<int, List<string>> adverbs = new Dictionary<int, List<string>>
    {
        {20, minor}, {40, moderate}, {60, major}, {-20, negative}
    };
    
    private void Start()
    {
        state = new Color(0, 255, 0, 256);
        stateImage.color = state;
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

        var change = new Tuple<int, int, int, int>(advVal * adjVal.Item1,
                                                   advVal * adjVal.Item2,
                                                   advVal * adjVal.Item3,
                                                   advVal * adjVal.Item4);
        
        Debug.Log("change = " + change);

        state = new Color(state[0]+change.Item1,
                          state[1]+change.Item2,
                          state[2]+change.Item3,
                          state[3]+change.Item4);

        stateImage.color = state;
        Debug.Log(state);


    }
    
    void Update()
    {
        for (int i = 0; i < 4; i++)
        {
            distance += Mathf.Pow(targetColor.target[i]- state[i],2);
        }

        distance = Mathf.RoundToInt(distance/4);
        Distance.text = "Distance: " + distance;
    }
}
 