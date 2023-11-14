package example;

import java.nio.file.Path;
import java.util.Scanner;

public final class Screen {
	
	private static Screen instance;
	
	private final Scanner sc = new Scanner(System.in);
	
	private final FileManager fm = FileManager.getInstance();
	
	
	private Screen() {}
	
	
	public static Screen getInstance() {
		if(instance == null) instance = new Screen();
		return instance;
	}
	
	public void play() {
		
		boolean stop = false;

		final String menu = """
			---------------------------
			1. Llistar directori
			2. Mostrar dades del fitxer
			3. Borrar fitxer
			4. Copiar fitxer
			5. Copiar directori
			6. Menejar fitxer
			7. Menejar directori
			8. Llegir fitxer xml
			9. Llegir fitxer txt
			0. Eixir del programa
			---------------------------
			Respuesta: 
			""";
		
		do {
			System.out.print(menu);
			int answ = sc.nextInt();
			
			
			switch (answ) {
				
				case 0 -> stop = true;
				case 1 -> fm.unix_ls(preguntarRutaExistent());
				case 2 -> fm.getFileData(preguntarRutaExistent());
				case 3 -> fm.deleteRoute(preguntarRutaExistent());
				case 4 -> fm.cpFile(preguntarRutaExistent(), preguntarRutaNova());
				case 5 -> fm.cpDirectory(preguntarRutaExistent(), preguntarRutaNova());
				case 6 -> fm.mvFile(preguntarRutaExistent(), preguntarRutaNova());
				case 7 -> fm.mvDirectory(preguntarRutaExistent(), preguntarRutaNova());
				case 8 -> fm.readXmlFile(preguntarRutaExistent());
				case 9 -> fm.readTxtFile(preguntarRutaExistent());
				default -> System.out.println("Opción incorrecta");
			
			}
			
		} while(!stop);
		
		sc.close();
		
	}

	private Path preguntarRuta() {
		System.out.print("Directori: ");
		return Path.of(sc.next());
	}
	
	private Path preguntarRutaExistent() {
		boolean stop = false;
		
		Path path;
		
		do {
			
			path = preguntarRuta();

			if (path.toFile().exists()) {
				stop = true;
			} else {
				System.out.println("Este directorio no existe!");
			}
			
		} while(!stop);
		
		return path;
	}

	private Path preguntarRutaNova() {
		boolean stop = false;

		Path path;

		do {

			path = preguntarRuta();

			if (path.getParent().toFile().exists()) {
				stop = true;
			} else {
				System.out.println("Este directorio padre no existe!");
			}

		} while(!stop);

		return path;
	}
	
}
