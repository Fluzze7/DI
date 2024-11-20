package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class CatalogActivity extends AppCompatActivity {
    private Button boton_detail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_catalog);

        // Ajustar las barras del sistema
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Inicializar el botón correctamente
        boton_detail = findViewById(R.id.catalog_button);

        // Configurar el listener
        boton_detail.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Navegar a la actividad DetailActivity
                Intent intent = new Intent(CatalogActivity.this, DetailActivity.class);
                startActivity(intent);
            }
        });
    }
}
