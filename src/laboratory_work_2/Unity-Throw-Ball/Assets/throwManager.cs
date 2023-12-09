using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class throwManager : MonoBehaviour {

    private Vector3 startPos; //mouse slide movement start pos
    private Vector3 endPos; //mouse slide movement end pos
    public float zDistance = 30.0f; //z distance
    public float rotationSpeed = 1.0f;
    public float torque = 5f;

    private bool isThrown;

    private Vector3 reflectionDir = new Vector3(0, 0, 0);

    public Rigidbody rb;

    private 

    void Start(){
        isThrown = false;
        rb = GetComponent<Rigidbody>();
    }

    void Update () {

        if (Input.GetKeyDown(KeyCode.R)) {
            SceneManager.LoadScene (0); // Reset scene on pressing R
        }

        if (isThrown)
        {
            return; //prevent user from accessing ball after being thrown
        }

        if (Input.GetMouseButtonDown (0)) {
            //get start mouse position
            Vector3 mousePos = Input.mousePosition * -1.0f;
            mousePos.z = zDistance; //add z distance

            startPos = Camera.main.ScreenToWorldPoint(mousePos);

            //Print start Pos for debugging
            Debug.Log (startPos);
        }

        if(Input.GetMouseButtonUp(0)){
            //get release mouse position
            Vector3 mousePos = Input.mousePosition * -1.0f;
            mousePos.z = zDistance; //add z distance

            // convert mouse position to world position
            endPos = Camera.main.ScreenToWorldPoint(mousePos);
            endPos.z = Camera.main.nearClipPlane; //removing this breaks stuff, no idea why though

            //Print start Pos for debugging
            Debug.Log (endPos);

            Vector3 throwDir = (startPos - endPos).normalized; //get throw direction based on start and end pos

            rb.AddForce(throwDir * (startPos - endPos).sqrMagnitude); //add force to throw direction * magnitude
            isThrown = true;
            //rb.AddRelativeTorque(reflectionDir * 5f, ForceMode.Force);
        }
    }

    private void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.CompareTag("Wall")) {
            // Calculate the reflection direction
            Vector3 reflectionDir = Vector3.Reflect(rb.velocity, collision.contacts[0].normal) * 0.85f;
            rb.velocity = reflectionDir;
            rb.AddRelativeTorque(reflectionDir * 2f, ForceMode.Force);
        }
    }
}
