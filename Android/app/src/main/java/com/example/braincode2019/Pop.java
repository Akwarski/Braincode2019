package com.example.braincode2019;

import android.app.Activity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.widget.TextView;

import java.util.List;

class Pop extends Activity {

    TextView tv1, tv2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.pop_window);

        DisplayMetrics dm  = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int)(width*.8),(int)(height*.6));

        /*List<JsonData> items = getIntent().getSerializableExtra("JsonData");

        for (JsonData item : items) {
            StringBuilder sb = new StringBuilder();
            sb.append("type: " + item.getType() + "\n");
            sb.append("name: " + item.getName() + "\n");
            sb.append("adress: " + item.getAdress() + "\n");
            sb.append("post code: " + item.getPost_code() + "\n");
            sb.append("city: " + item.getCity() + "\n");
            sb.append("dlugosc: " + item.getDlugosc() + "\n");
            sb.append("szerokosc: " + item.getSzerokosc() + "\n \n");
            //sb.append("dates: " + item.getDates() + "\n");

            tv2.append(sb);
        }*/
    }
}