@ArchTest
public static final ArchRule noRawHttpClient = noClasses()
    .should().dependOnClassesThat()
        .haveFullyQualifiedName("org.springframework.web.client.RestTemplate")
    .orShould().dependOnClassesThat()
        .haveFullyQualifiedName("java.net.HttpURLConnection")
    .orShould().dependOnClassesThat()
        .haveFullyQualifiedName("org.apache.http.client.HttpClient")
    .as(
        "❌ 禁止直接使用 RestTemplate / HttpURLConnection / Apache HttpClient。\n" +
        "✅ FIX: 注入统一的 API Client:\n" +
        "    private final ApiClient apiClient; // 构造器注入\n" +
        "    Foo foo = apiClient.get(\"/endpoint\", Foo.class);\n" +
        "📖 See: docs/conventions/api-calls.md"
    );