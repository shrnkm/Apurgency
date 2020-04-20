using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class DistanceCalculator : MonoBehaviour
{
    public TextMeshProUGUI Distance;
    
    private float distance = 0;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        for (int i = 0; i < 4; i++)
        {
            distance += Mathf.Pow(targetColor.target[i]- stateColor.state[i],2);
        }

        distance = Mathf.RoundToInt(Mathf.Sqrt(distance));
        Distance.text = "Distance: " + distance;

    }
}
