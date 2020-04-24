using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class targetColor : MonoBehaviour
{
    public static Color target = new Color(255, 0, 0, 256);
    public Image targetImage;

    void Start()
    {
        targetImage.color = target;

    }
}
