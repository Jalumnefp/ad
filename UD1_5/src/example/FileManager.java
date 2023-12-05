package example;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.nio.file.*;
import java.nio.file.attribute.FileAttributeView;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public final class FileManager {
	
	private static FileManager instance;
	
	private FileManager() {}

	private String test = "test";

	
	public static FileManager getInstance() {
		if (instance == null) instance = new FileManager();
		return instance;
	}
	
	public void unix_ls(Path path) {
		
		if(path.toFile().isDirectory()) {
			
			try (DirectoryStream<Path> directory = Files.newDirectoryStream(path)) {
				
				directory.forEach(it -> {
					File file = it.toFile();
					System.out.printf("%s %s\n", file.getName(), file.isFile() ? 'f' : 'd');
				});
				
			} catch (IOException e) {
				// TODO: handle exception
			}
			
		} else {
			System.out.println("Ruta incorrecta. Asegurate de seleccionar un directiorio.");
		}

	}
	
	public void getFileData(Path path) {
		if (path.toFile().isFile()) {
			
			String nameFile = path.toFile().getName();
			String sizeFile = String.valueOf(path.toFile().getTotalSpace());
			long modHours = path.toFile().lastModified();
			LocalDateTime date = LocalDateTime.ofInstant(Instant.ofEpochMilli(modHours), ZoneId.systemDefault());
			String lastModFile = date.toString().replace('T', ' ');
			
			System.out.printf("== INFO ==\nNom: %s\nSize: %s\nFecha de la ultima modificacion: %s\n", nameFile, sizeFile, lastModFile);
		} else {
			System.out.println("Ruta incorrecta. Asegurate de seleccionar un fichero.");;
		}

	}
	
	public void deleteRoute(Path path) {
		
		if (path.toFile().isFile()) {
			try {
				Files.deleteIfExists(path);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} else {
			System.out.println("No es un fichero.");
		}
			
	}
	
	public void cpFile(Path inputPath, Path outputPath) {
		
		if (inputPath.toFile().isFile()) {
			try {
				Files.copy(inputPath, outputPath, StandardCopyOption.REPLACE_EXISTING);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} else {
			System.out.println("No es un fichero.");
		}
		
	}
	
	public void mvFile(Path inputPath, Path outputPath) {
		
		if (inputPath.toFile().isFile()) {
			try {
				Files.move(inputPath, outputPath, StandardCopyOption.REPLACE_EXISTING);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} else {
			System.out.println("No es un fichero.");
		}
		
	}

	private void createDirectoryIfNotExists(Path path) {
		try {
			if (!path.toFile().exists())
				Files.createDirectory(path);
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	private List<Path> getChildPaths(Path path) {
		List<Path> pathList = new ArrayList<>();

		if(path.toFile().isDirectory()) {

			try (DirectoryStream<Path> directory = Files.newDirectoryStream(path)) {

				directory.forEach(it -> {
					pathList.add(it);
					if (it.toFile().isDirectory()) {
						pathList.addAll(getChildPaths(it));
					}
				});

			} catch (IOException e) {
				// TODO: handle exception
				e.printStackTrace();
			}

		} else {
			System.out.println("Ruta incorrecta. Asegurate de seleccionar un directiorio.");
		}

		return pathList;
	}
	
	public void cpDirectory(Path inputPath, Path outputPath) {

		createDirectoryIfNotExists(outputPath);

		List<Path> pathList = getChildPaths(inputPath);

		pathList.forEach(path -> {
			Path newPath = Path.of(outputPath + File.separator + inputPath.relativize(path));

			try {
				Files.copy(path, newPath, StandardCopyOption.REPLACE_EXISTING);
			} catch (IOException e) {
				e.printStackTrace();
			}

		});

	}
	
	public void mvDirectory(Path inputPath, Path outputPath) {

		try {
			Files.move(inputPath, outputPath, StandardCopyOption.REPLACE_EXISTING);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public void readXmlFile(Path path) {
		System.out.println("<persones>");
		DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
		try {
			DocumentBuilder docBuilder = dbFactory.newDocumentBuilder();
			Document doc = docBuilder.parse(path.toFile());
			NodeList root = doc.getElementsByTagName("persona");

			for (int i = 0; i < root.getLength(); i++) {
				Node nodo = root.item(i);
				if (nodo.getNodeType() == Node.ELEMENT_NODE) {
					NodeList childs = nodo.getChildNodes();

					for (int j = 0; j < childs.getLength(); j++) {
						if (j == 0) {
							System.out.println("\t<" + nodo.getNodeName() + ">");
						}
						Node child = childs.item(j);
						if (child.getNodeType() == Node.ELEMENT_NODE) {

							System.out.printf("\t\t<%s>%s</%s>\n", child.getNodeName(), child.getTextContent(), child.getNodeName());
						}
						if (j == childs.getLength()-1) {
							System.out.println("\t</" + nodo.getNodeName() + ">");
						}
					}
				}
			}
			System.out.println("</persones>");


		} catch (ParserConfigurationException | IOException | SAXException e) {
			throw new RuntimeException(e);
		}

	}
	
	public void readTxtFile(Path path) {
		try(InputStream is = Files.newInputStream(path, StandardOpenOption.READ)) {
			
			
			int temp;
			while ((temp = is.read()) != -1) {
				System.out.print((char)temp);
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	
}
