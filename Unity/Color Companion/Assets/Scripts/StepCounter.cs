using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class StepCounter : MonoBehaviour
{
    public TextMeshProUGUI stepsStr;
    private int stepsInt = 0;
    
    public void Counter()
    {
        stepsInt += 1;
        stepsStr.text = "Steps: " + stepsInt;
    }
}
