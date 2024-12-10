
import folium

# Create a map
m = folium.Map(location=[35.776768257824415, 35.23451634480424], zoom_start=4)

# Add a combined title and instructions box with a toggle button positioned above the title box
title_instructions_html = '''
<div id="toggleButtonWrapper" style="
    position: fixed; 
    top: 5px; left: 50px; 
    z-index: 10000;
">
    <button id="toggleButton" style="
        font-size: 14px; font-weight: bold; 
        background-color: #007bff; color: white; 
        padding: 5px 10px; 
        border: none; border-radius: 5px; 
        cursor: pointer; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    ">
        Hide Title
    </button>
</div>
<div id="titleBox" style="
    position: fixed; 
    top: 40px; left: 50px; 
    font-size: 26px; font-weight: bold; 
    text-align: center; background-color: #343a40; 
    color: white; padding: 10px 20px; 
    border-radius: 10px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
    border: 2px solid #007bff; z-index: 9999;
">
    Explore Israel's Periphery Doctrine
    <div style="
        font-size: 14px; 
        margin-top: 10px; 
        font-weight: normal;
        text-align: left;
    ">
        Start by clicking on Israel to learn about the policy of periphery<br>Tips:<br>(1) The map shifts, click and drag to move around<br>(2) Click the 'hide title' button if this title box is obscuring any text<br>(3) Click on the 'x' in the top-right or simply off of the pop-up to hide it
    </div>
</div>

<script>
    // JavaScript to toggle the title box visibility
    document.getElementById('toggleButton').addEventListener('click', function () {
        var titleBox = document.getElementById('titleBox');
        var button = document.getElementById('toggleButton');
        if (titleBox.style.display === 'none') {
            titleBox.style.display = 'block';
            button.innerHTML = 'Hide Title';
        } else {
            titleBox.style.display = 'none';
            button.innerHTML = 'Show Title';
        }
    });
</script>
'''

# Add the title and toggle button to the map
m.get_root().html.add_child(folium.Element(title_instructions_html))


# Function to add markers with centering and auto-popup adjustment
def add_marker(map_object, location, tooltip, popup, icon):
    marker = folium.Marker(
        location=location,
        tooltip=tooltip,
        popup=popup,
        icon=icon
    )
    marker.add_to(map_object)
    
    # JavaScript to ensure the popup is fully visible and the map recenters
    script = f"""
    <script>
    var marker = {marker.get_name()};
    marker.on('click', function(e) {{
        var popup = marker.getPopup();
        popup.on('add', function() {{
            map.panTo(marker.getLatLng(), {{
                animate: true
            }});
        }});
    }});
    </script>
    """
    map_object.get_root().html.add_child(folium.Element(script))

# Add markers

add_marker(m, [33.8547, 35.8623], 'Lebanon',
           """
           <h1 style='text-align: center;'>Lebanon</h1>
           <img src='sla.jpg' width=500px style='display: block; margin: 0 auto;'>
           <p style='text-align: center;'><em>Major Saad Haddad and Christian militias from South Lebanon occupy Chateau de Beaufort after its capture by the Israeli army on June 7, 1982, Lebanon.</em></p>
           <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.6; padding: 10px; width: 600px;'>
               <p><strong>The relationship between Israel and the Maronites:</strong> The largest Christian community in Lebanon, the Maronites, have had a relationship with Israel shaped by both cooperation and mutual anxieties, rooted in their shared sense of marginalization within a predominantly Muslim region. Although Israel’s Periphery Doctrine’s stated aim is to form alliances with non-Arab groups and states to counter Arab hostility, it is important to note what “Arab” means. Lebanese Christian families are credited with the creation of a modern Arab identity based upon a shared language in hopes of integrating into society further and curbing any future persecution. While some Maronites identify themselves with an Arab identity—and many do not, instead tracing their roots to the Ancient Phoenicians or Assyrian peoples—the relationship between Israel and the Maronites was generally focused on countering mutual Arab-Muslim actors. This relationship, despite moments of alignment, has ultimately been characterized by disappointment and unfulfilled potential.</p>
               
               <p><strong>Early Cooperation:</strong> The foundation for Israeli-Maronite relations was laid in the early 20th century, driven by mutual concerns over their vulnerability in the Arab-dominated Middle East. In 1920, Zionist and Maronite activists signed an agreement recognizing the Jews' right to establish a national home in Palestine in exchange for recognizing an independent Christian Lebanon separate from Syria. This cooperation reflected shared aspirations for autonomy and a desire to avoid Arab and Muslim dominance. The relationship was further solidified in 1946 when the Maronite Church and the Jewish Agency signed a treaty emphasizing cooperation based on the principle of "isolation from and hostility towards their Arab-Muslim surroundings" (Hazran 2020).</p>
               
               <p><strong>Shifts in the 20th Century:</strong> By the mid-1930s, the Maronite political orientation began to shift with the rise of the concept of "Greater Lebanon." Promoted by figures like Bishara al-Khuri, this idea emphasized coexistence with the Muslim population and closer ties to neighboring Arab countries. As the Maronite leadership increasingly embraced this vision, their stance toward Israel shifted to neutrality or hostility, motivated by the need to maintain internal stability in Lebanon and preserve the principles of the "National Charter" (Zisser 1995).</p>
               
               <p>Despite these shifts, points of cooperation persisted. During the 1958 Lebanese Civil War, Israel supported the Maronite-led Kataeb Party to counter Arab nationalist forces. In the 1970s, as Lebanon's civil war escalated, Israel rekindled its ties with Maronite factions, particularly the Lebanese Front. Both sides felt increasingly threatened by Palestinian armed groups and Syrian intervention (Zisser 1995).</p>
               
               <p><strong>The 1982 Israeli Invasion:</strong> The most pivotal moment came with Israel's 1982 invasion of Lebanon, codenamed "Operation Peace for Galilee." Initially aimed at eliminating PLO bases, the invasion was also motivated by Israel's vision of a Maronite-dominated state aligned with its interests. Israeli officials, including Defense Minister Ariel Sharon, developed close ties with Maronite leader Bachir Gemayel, who was elected President of Lebanon with Israeli support (Zisser 1995). However, Gemayel’s assassination, the Sabra and Shatila massacre, and Israel's prolonged occupation marred the operation, generating widespread condemnation (Rojhilat, et. al. 2018). Israel’s strategic goals failed, leading to disillusionment with the Maronites.</p>
               
               <p><strong>Aftermath and Decline:</strong> The aftermath of the 1982 invasion marked the end of Israel's "Minorities Alliance" policy. The complexities of Lebanese politics, the rise of Hezbollah, and Israel’s military entanglement led to growing frustration. Despite Israel’s initial strategic interest in a "Christian Lebanon," the Maronites were ultimately blamed for Israel's perceived failure in Lebanon. This breakdown exemplified the limitations of the Periphery Doctrine in fostering lasting alliances amid regional complexities and Lebanese political dynamics.</p>
               
               <p><strong>Sources:</strong></p>
               <ul>
                   <li>Hazran, Y. (2020). <em>The Maronites and Israel: The Politics of Minorities in the Middle East.</em> Journal of Middle Eastern Studies.</li>
                   <li>Zisser, E. (1995). <em>The Maronites, Israel, and the Arab-Israeli Conflict.</em> Middle Eastern Studies, 31(3), 605–622.</li>
                   <li>Rojhilat, S., & Romano, D. (2018). <em>Israel’s periphery doctrine and the Kurds.</em> In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
               </ul>
           </div>
           """,
           folium.Icon(icon='cross', prefix='fa', color='red'))





add_marker(m, [35.721399227207556, 51.36824024219843], 'Iran',
           """
           <h1 style='text-align: center;'>Iran</h1>
           <img src='Iran_Israel.jpg' width=500px style='display: block; margin: 0 auto;'>
           <p style='text-align: center;'><em>Top Iranian military officials meet with Israeli officers in the headquarters of the Israel Defense Forces, 1975.</em></p>
           <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.5; padding: 10px; width: 600px;'>
               <p><strong>The historical relationship between Israel and Iran</strong> offers a nuanced narrative of ancient connections, strategic alliances, and bitter rivalry, evolving significantly over centuries. Rooted in ancient ties, the Jewish and Persian peoples shared a notable cultural and historical affinity. Persian King Cyrus the Great, celebrated in Jewish tradition for liberating Jews from Babylonian captivity in the 6th century BCE, laid the foundation for a relationship marked by mutual respect. Persian lands later became a center for flourishing Jewish communities (Ansari 2024).</p>
               
               <p><strong>Iran under the Shah’s Regime:</strong> The 20th century ushered in a period of strategic cooperation between Israel and Iran. Under the Shah, Israel and Iran’s partnership flourished, marked by robust military, intelligence, and economic cooperation. Shared concerns over pan-Arabism, led by Egypt’s Gamal Abdel Nasser, and the Soviet Union’s regional ambitions drove this partnership (Rojhilat, et. al. 2018). Iran became a cornerstone of Israel’s policy of periphery doctrine.</p>
               
               <p>Israel provided Iran with advanced weaponry, including Gabriel missiles and communication systems, and trained the SAVAK, Iran’s secret police. Intelligence-sharing focused on regional threats like Egypt, Iraq, and communist movements. Economically, Iran was a vital market for Israeli arms and a critical alternative oil supplier during crises such as the 1973 oil embargo (Furlan 2022). The partnership extended to supporting Kurdish insurgents in northern Iraq, a move aimed at weakening Iraq—a mutual adversary—and preventing its alignment with Arab forces against Israel. These efforts underscored a pragmatic, mutually beneficial alliance. Iran remained relatively neutral on the Palestinian issue, balancing support for fellow Muslims, a fear of rising Sunni power, and a strategic alliance with Israel.</p>
               
               <p><strong>Iran under the Ayatollah’s Regime:</strong> The 1979 Islamic Revolution, however, marked a turning point, replacing the Shah’s regime with Ayatollah Ali Khomeini’s theocratic government. The new regime declared Israel an enemy, framing its ideology around anti-Zionism and transforming Iran from a key ally into a primary regional adversary (Voller 2015). This ideological shift was further underscored by Iran’s support for groups like Hezbollah and its pursuit of strategies aimed at undermining Israel’s security.</p>
               
               <p>Despite the deep animosity, a pragmatic episode occurred during the Iran-Iraq War (1980–1988) with the Iran-Contra Affair. Israel covertly supplied arms to Iran, mediated by the United States, in a bid to weaken Iraq (Furlan 2022). However, this cooperation was fleeting, and the underlying hostility persisted. Iran’s subsequent "Ring of Fire" strategy, involving proxy forces and missile bases encircling Israel, has escalated tensions (Furlan 2022). These proxies, which include Hamas in the Palestinian Territories, Hezbollah in Lebanon, and the Houthis in Yemen, have all used the plight of the Palestinians as justification for attacks on Israel while providing plausible deniability to their principal Iran. The Abraham Accords, normalizing relations between Israel and several Arab states, have further alarmed Tehran, heightening regional competition.</p>
               
               <p><strong>Conclusion:</strong> This intricate history, from ancient kinship to modern enmity, highlights the volatility of geopolitics in the Middle East and the goal of the Periphery Doctrine. Once a strategic partnership shaped by Cold War dynamics, Israeli-Iranian relations now epitomize the enduring impact of ideological divides, regional rivalries, and an actively changing balance of power in the Middle East.</p>
               
               <p><strong>Sources:</strong></p>
               <ul>
                   <li>Ansari, A. (2024). <em>The Shallow Roots of Iran’s War with Israel: Beneath Tehran’s Extremism, a Lost History of Deep Iranian-Jewish Ties.</em> Foreign Affairs Magazine. <a href='https://www.foreignaffairs.com/israel/shallow-roots-irans-war-israel' target='_blank'>Link</a></li>
                   <li>Furlan, M. (2022). <em>Israeli-Iranian relations: past friendship, current hostility.</em> Israel Affairs, 28(2), 170–183. <a href='https://doi.org/10.1080/13537121.2022.2041304' target='_blank'>Link</a></li>
                   <li>Rojhilat, S., & Romano, D. (2018). <em>Israel’s periphery doctrine and the Kurds.</em> In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
                   <li>Voller, Y. (2015). <em>From Periphery to the Moderates: Israeli Identity and Foreign Policy in the Middle East.</em> Political Science Quarterly, 130(3), 505–535. <a href='http://www.jstor.org/stable/43828693' target='_blank'>Link</a></li>
               </ul>
           </div>
           """,
           folium.Icon(icon='mosque', prefix='fa', color='red'))




add_marker(m, [39.94593856201844, 32.85303677231913], 'Turkey',
           """
           <h1 style='text-align: center;'>Turkey</h1>
           <img src='Esin_Weizmann.jpg' width=500px style='display: block; margin: 0 auto;'>
           <p style='text-align: center;'><em>The first Turkish ambassador to Israel, Seyfullah Esin (center), with President Chaim Weizmann (left) and Foreign Minister Moshe Sharett (right), after submitting his credentials in Rehovot.</em></p>
           <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.6; padding: 10px; width: 600px;'>
               <p><strong>Early Relationship with Israel:</strong> Turkey was the first Muslim-majority country to formally recognize Israel in March 1949 (Rojhilat, et. al. 2018). However, its relationship with Israel during the early years of Ben-Gurion's Periphery Doctrine was cautious and complex. While Turkey shared Israel’s concerns over regional threats such as pan-Arabism under Egypt’s Gamal Abdel Nasser, its engagement in the Periphery Doctrine was less enthusiastic than that of Iran or Ethiopia. Turkey's relatively warmer relations with Arab states, reliance on Arab oil, and access to American aid through NATO membership contributed to its measured approach (Voller 2025).</p>

                <p><strong>1950s-1980:</strong> Despite this caution, shared strategic concerns fostered collaboration between Turkey and Israel. Syria's territorial claims on southern Turkey, the Soviet-Syrian Treaty of 1957, and Nasser’s growing regional influence drove Turkey closer to Israel. The late 1950s saw a series of covert meetings between Israeli and Turkish officials, including a top-secret visit by Israeli Prime Minister David Ben-Gurion to meet Turkish Prime Minister Adnan Menderes. These efforts led to the elevation of Turkish-Israeli diplomatic relations, culminating in the establishment of a Turkish embassy in Tel Aviv by 1980 (Rojhilat, et. al. 2018).</p>

                <p>Turkey’s strategic alliance with Israel was balanced against its public sensitivity to the Palestinian issue. Events such as the Israeli annexation of East Jerusalem in 1980 and the UN resolution equating Zionism with racism in 1975 prompted Turkey to maintain a cautious public stance (Jewish Virtual Library). Nonetheless, the alliance yielded significant military, economic, and security benefits for both countries. For Israel, this relationship became even more critical following the 1979 Iranian Revolution, which removed a key Periphery Doctrine partner.</p>

                <p><strong>2000s and the Rise of AKP:</strong> The rise of Turkey’s Justice and Development Party (AKP) in 2002 marked a sharp decline in Turkish-Israeli relations. The AKP's Islamist-leaning policies, coupled with the diminishing influence of Turkey’s military—a staunch supporter of the alliance with Israel—reshaped the bilateral dynamic. Under AKP leadership, Turkey distanced itself from Israel, adopting a more critical stance on the Palestinian issue. Ankara’s condemnation of Israeli actions in Gaza, its support for Hamas, and strained diplomatic relations, including incidents like the 2010 Mavi Marmara flotilla confrontation, underscored the end of the strategic partnership (Jewish Virtual Library).</p>

                <p>During the war following Hamas’ October 7th attacks, Erdogan has vocalized his support for Iranian proxies and condemned Israel’s actions. In the aftermath of the fall of the Assad regime in Syria and the weakening of Iranian proxies, Turkey’s influence in the region is bolstered and could increase future tensions between Turkey and Israel.</p>

                <p>The robust alliance fostered during the Periphery Doctrine era gradually dissolved as Turkey aligned its foreign policy with new ideological and regional priorities. While the AKP’s tenure has been marked by significant tension, the early decades of Turkish-Israeli relations remain a significant example of Ben-Gurion's strategy to forge alliances with non-Arab states to counter regional isolation, and exemplify how the Israeli-Palestinian issue can strain relationships between nations.</p>

               <ul>
                   <li>Jewish Virtual Library. <em>Israel-Turkey Relations.</em> Last updated November 2024. <a href='https://www.jewishvirtuallibrary.org/turkey-israel-relations' target='_blank'>Link</a></li>
                   <li>Rojhilat, S., & Romano, D. (2018). <em>Israel’s periphery doctrine and the Kurds.</em> In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
                   <li>Voller, Y. (2015). <em>From Periphery to the Moderates: Israeli Identity and Foreign Policy in the Middle East.</em> Political Science Quarterly, 130(3), 505–535. <a href='http://www.jstor.org/stable/43828693' target='_blank'>Link</a></li>
               </ul>
           </div>
           """,
           folium.Icon(icon='star-and-crescent', prefix='fa', color='red'))



add_marker(m, [9.008269260071042, 38.74792799907618], 'Ethiopia',
           """
           <h1 style='text-align: center;'>Ethiopia</h1>
           <img src='Haile_Golda.jpeg' width=500px style='display: block; margin: 0 auto;'>
           <p style='text-align: center; style=font-style: italic;'>Israeli Prime Minister Golda Meir shaking hands with Ethiopian Emperor Haile Selassie</p>
           <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.5; padding: 10px; width: 600px;'>
               <p>Ethiopia became a key component of Israel’s Periphery Doctrine due to a combination of shared concerns, strategic importance, and historical affinity. Both Israel and Ethiopia, a predominantly Christian nation, felt threatened by the rising tide of pan-Arabism and socialist expansion, particularly the influence of Egyptian President Gamal Abdel Nasser. Their common fear of pan-Arab nationalism and the potential for Islamic unity in the Horn of Africa further united their interests (Bishku 1994).</p>
               
               <p>Strategically, Ethiopia’s control of the Red Sea coastline (prior to the secession of Eritrea) made it an invaluable ally to Israel, especially in terms of maritime security. The Red Sea was a vital trade route for Israel, and Ethiopia's position provided Israel with critical access (Rojhilat, et. al. 2018). Additionally, Ethiopia served as a conduit for Israeli assistance to South Sudanese rebels and played a key role in the rise of Ugandan dictator Idi Amin, further demonstrating its geopolitical importance (Hazran 2020).</p>
               
               <p>The relationship was also shaped by historical and cultural ties. Ethiopian Emperor Haile Selassie, who regarded himself as the "Lion of Judah," felt a deep historical connection to Israel, rooted in the Ethiopian narrative that linked the country’s Solomonic dynasty to King Solomon and the Queen of Sheba (Bishku 1994). This shared legacy of Jewish heritage strengthened the diplomatic bonds between the two nations, leading to the establishment of formal relations in 1956.</p>
               
               <p>Israel and Ethiopia’s relationship developed into a "special relationship," marked by extensive cooperation in various sectors. Militarily, Israel provided significant support, including military training for Ethiopian forces, especially during the Eritrean rebellion and the Ogaden War—both of which were supported by Arab states. Israel also assisted Ethiopia with economic and technical cooperation, working on projects such as developing the country’s blood bank, ports, and fisheries (Rojhilat, et. al. 2018). Additionally, Ethiopia played a crucial role in Israel's airlifting of Ethiopian Jews during Operations Moses and Solomon, allowing thousands of Ethiopian Jews to immigrate to Israel (Bishku 1994).</p>
               
               <p>Despite changes in the political landscape, Ethiopia largely refrained from following the broader African trend of severing ties with Israel. Even in 1973, when Ethiopia did break off diplomatic relations, it was more a pragmatic move to align with the African bloc rather than a reflection of hostility towards Israel. Ethiopia abstained from UN General Assembly Resolution 3379, which equated Zionism with racism, unlike many other African nations (Bishku 1994). Even after the Marxist Derg regime came to power in 1974, Ethiopia continued discreet engagement with Israel, highlighting the continued strategic importance of the relationship (Bishku 1994).</p>
               
               <p>The enduring cooperation between Israel and Ethiopia is a testament to the principles of the Periphery Doctrine. It demonstrates how Israel built alliances based on shared security concerns, leveraged strategic partnerships to break regional isolation, and gained access to critical resources and intelligence. The Israeli-Ethiopian alliance, even in the face of shifting geopolitical dynamics, underscores the enduring relevance of the Periphery Doctrine and its role in navigating the complexities of Middle Eastern and African geopolitics.</p>

               <p><strong>Sources:</strong></p>
               <ul style="font-size: 14px;">
                   <li>Bishku, Michael. (1994). Israel and Ethiopia: From a Special to a Pragmatic Relationship. Conflict Quarterly. 14. 39-62.</li>
                   <li>Hazran, Y. (2020). A people that shall dwell alone; is that so? Israel and the minorities alliance. Middle Eastern Studies, 56(3), 396–411. https://doi.org/10.1080/00263206.2020.1713758</li>
                   <li>Rojhilat, S., & Romano, D. (2018). Israel’s periphery doctrine and the Kurds. In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
               </ul>
           </div>
           """,
           folium.Icon(icon='book-bible', prefix='fa', color='red'))



add_marker(
    m, 
    [37.22948346482641, 42.74054281872922], 
    'The Kurds',
    """
    <h1 style='text-align: center;'>The Kurds</h1>
    <img src='Amir_Kurds.webp' width=500px style='display: block; margin: 0 auto;'>
    <p style='text-align: center; style=font-style: italic;'>The head of Israel’s Mossad, General Meir Amit, in dark clothing, met with the Kurdish leader Mulla Mustafa Barzani in the Kurdistan mountains (circa 1966).</p>
    <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.5; padding: 10px; width: 600px;'>
        <p>The relationship between Israel and the Kurds has long been a significant, though often understated, aspect of Israel's Periphery Doctrine. The majority of Kurdish people are non-Arab Muslims with minority populations in Turkey, Iran, Iraq, and Syria. Both the Jews and the Kurds share a history of persecution by common adversaries, particularly Arab nationalists and extremist regimes. For instance, Saddam Hussein's regime in Iraq, known for its hostility toward Israel, also perpetrated genocide against the Kurds (Frantzman 2024). Similarly, Hafez Assad's regime in Syria denied citizenship and basic rights to many Kurds, while Iran’s ayatollahs systematically suppressed Kurdish dissidents. This shared experience of repression forged a natural bond between the two peoples, united in their desire for self-determination and security.</p>
        <p>The genesis of Israeli-Kurdish relations can be traced back to the 1960s, following the outbreak of the Kurdish rebellion against the Iraqi government in 1961. This marked the beginning of a growing alliance, rooted in Israel's Periphery Doctrine, which sought to build partnerships with non-Arab states and groups in the Middle East to counter the Arab opposition to Israel. The Kurds, with their longstanding insurgency against the Iraqi government—a staunch supporter of anti-Israeli policies—offered Israel a valuable opportunity for cooperation (Rojhilat, et. al. 2018). Additionally, the Kurdish movement had limited ties to the Kurdistan Workers' Party (PKK) active in Turkey, reducing the risk of significant diplomatic fallout for Israel from Turkey or the United States.</p>
        <p>The relationship began in earnest when Ismet Sherif Vanli, a Kurdish activist, visited Israel with the approval of Mustafa Barzani, leader of the Kurdistan Democratic Party (KDP). During his visit, Vanli met with Israeli Prime Minister Levi Eshkol and Shimon Peres, then-head of the Labor Party. This visit laid the groundwork for deeper cooperation (Frantzman 2024). Following this, Israeli support expanded in several key areas, including military training, humanitarian aid, and logistical assistance. Israeli military commanders were sent to Kurdish-controlled areas in northern Iraq to train the Peshmerga forces, and field hospitals were set up to provide medical support. Israel also facilitated connections for the Kurds with the outside world and gathered intelligence on Iraqi military movements.</p>
        <p>One of the most significant instances of Israeli assistance came during the Battle of Ali Beg Waterfall in 1965-1966, where Israeli Lieutenant Colonel Tsuri Sagay devised a successful defensive strategy for the Kurdish forces, who were vastly outnumbered by the Iraqi army. This cooperation, which included training Kurdish officers in Israel, marked a high point in Israeli-Kurdish relations and demonstrated the effectiveness of their military collaboration (Quitaz 2023).</p>
        <p>However, the alliance faced a setback in 1975 with the signing of the Algiers Accord between the Shah of Iran and Saddam Hussein. Under this agreement, Iran ceased its support for the Kurdish rebellion in exchange for territorial concessions from Iraq. As a result, Iranian support for the Kurds was withdrawn, and Israeli advisors were forced to leave Iraq (Rojhilat, et. al. 2018). The Kurdish rebellion was crushed, leading to a sense of betrayal among the Kurds. Despite this, the shared history of cooperation and mutual interests laid the foundation for the eventual re-emergence of ties in the post-Saddam era (Quitaz 2023).</p>
        <p>The relationship between Israel and the Kurds was revived after the fall of Saddam Hussein in 2003, as the Kurds established a de facto state in northern Iraq. Leaders like Masoud Barzani openly advocated for diplomatic relations with Israel, and Kurdish officials, such as Jalal Talabani, publicly embraced Israeli counterparts (Quitaz 2023). Despite facing significant opposition—such as the 2017 Kurdish independence referendum, during which the display of Israeli flags by Kurdish supporters was used by Iran and Turkey to stoke anti-Kurdish sentiment—the bond between Israel and the Kurds remains resilient. This relationship continues to reflect mutual security interests and shared aspirations for stability and recognition in a region fraught with complex geopolitical challenges.</p>
        <p>Despite the obstacles, the enduring ties between Israel and the Kurds remain rooted in their shared history of persecution and a mutual commitment to self-determination. As both groups continue to navigate a complex and volatile regional landscape, their alliance serves as a testament to the lasting relevance of Israel’s Periphery Doctrine (Frantzman 2024).</p>
        <p><strong>Sources:</strong><br>
        <ul>
            <li>Frantzman, S. (2024). Why did Israel’s new foreign minister embrace the Kurdish people? Foundation for Defense of Democracies. <a href="https://www.fdd.org/analysis/op_eds/2024/11/10/why-did-israels-new-foreign-minister-embrace-the-kurdish-people/">Link</a></li>
            <li>Rojhilat, S., & Romano, D. (2018). Israel’s periphery doctrine and the Kurds. In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
            <li>Quitaz, S. (2023). The Historic Ties between Israel and the Kurds of Iraq Will Continue Jerusalem Center for Security and Foreign Affairs. <a href="https://jcpa.org/article/the-historic-ties-between-israel-and-the-kurds-of-iraq-will-continue/">Link</a></li>
        </ul>
        </p>
    </div>
    """,
    folium.Icon(icon='mountain', prefix='fa', color='red')
)



add_marker(
    m, 
    [31.776768257824415, 35.23451634480424], 
    'Israel',
    """
    <h1 style='text-align: center;'>Israel: Ben Gurion's Periphery Doctrine</h1>
    <img src='ben_gurion.jpg' width=500px style='display: block; margin: 0 auto;'>
    <p style='text-align: center; style=font-style: italic;'>David Ben Gurion, the first Prime Minister of the State of Israel, at the 22nd Zionist Congress in 1946.</p>
    <div style='height: 250px; overflow-y: scroll; font-size: 16px; line-height: 1.5; padding: 10px; width: 600px;'>
        <p>Israel's Periphery Doctrine, conceived by Israel’s first prime minister, David Ben-Gurion, emerged as a strategic response to the united Arab opposition that threatened Israel's existence following its Declaration of Independence in 1948. Faced with isolation in a hostile region, the Policy sought to counterbalance the Arab bloc by forging alliances with non-Arab and non-Muslim states, as well as with minority groups in the Middle East (Hazran 2020). These alliances were designed to break the unity of Israel’s adversaries, reduce its diplomatic and economic isolation, and secure critical resources and intelligence. In the context of the Israeli-Palestinian conflict, the policy worked as an “outside-in” strategy: solve the conflict with the neighbors, before you solve the internal conflict.</p>
        <p>Key allies under the Periphery Doctrine included Ethiopia, Iran, Turkey, Lebanese Maronite Christians, and the Kurds (Rojhilat, et. al. 2018). Ethiopia's Christian identity and strategic location on the Red Sea made it a valuable partner, providing Israel with access to South Sudanese rebels and eventually facilitating the evacuation of Ethiopian Jews through Operations Moses and Solomon (Bishku 1994). Iran, sharing Israel's opposition to Egyptian President Nasser's Pan-Arabism, cooperated in areas such as oil, trade, and military support (Furlan 2022). Turkey, concerned about Soviet and Syrian influence, developed strategic ties with Israel, including military and intelligence collaboration. Lebanese Christians, due to their proximity and shared minority status, were seen as potential partners, with Israel even contemplating support for a Christian state in Lebanon (Zisser 1995). Similarly, Israel cultivated ties with the Kurdish resistance, recognizing their struggle against Arab-dominated governments as a shared interest.</p>
        <p>These alliances aimed to weaken Arab unity, secure vital resources like oil—particularly crucial during the 1973 oil crisis—and enhance Israel’s intelligence capabilities. For example, support for the Iraqi Kurds provided insights into the military and political dynamics of hostile neighboring states (Furlan 2022). Despite its initial successes, the policy faced significant setbacks, such as the 1979 Islamic Revolution in Iran, which transformed a key ally into a hostile regime, and the rise of Turkey’s pro-Islamic AKP in 2002, straining previously strong ties (Voller 2015).</p>
        <p>Nonetheless, the Periphery Doctrine underlying principles remain relevant. Some criticize the “outside-in” strategy as simply neglecting the Israeli-Palestinian issue. Others view major external threats like Iran as more pressing for the state than political negotiations about internal disputes and border issues. The changing Middle East, with the fall of the Assad-regime in Syria, the weakening of Iran’s Ring of Fire and their continued momentum towards obtaining nuclear weapons, and looming Israeli-Saudi normalization will affect whether Israel continues to pursue a policy of periphery.</p>
        <p><strong>Sources:</strong><br>
        <ul>
            <li>Bishku, Michael. (1994). Israel and Ethiopia: From a Special to a Pragmatic Relationship. Conflict Quarterly, 14. 39-62.</li>
            <li>Furlan, M. (2022). Israeli-Iranian relations: past friendship, current hostility. Israel Affairs, 28(2), 170–183. <a href="https://doi.org/10.1080/13537121.2022.2041304">Link</a></li>
            <li>Hazran, Y. (2020). A people that shall dwell alone; is that so? Israel and the minorities alliance. Middle Eastern Studies, 56(3), 396–411. <a href="https://doi.org/10.1080/00263206.2020.1713758">Link</a></li>
            <li>Rojhilat, S., & Romano, D. (2018). Israel’s periphery doctrine and the Kurds. In Federalism, secession, and international recognition regime (pp. 164-181). Routledge.</li>
            <li>Voller, Y. (2015). From Periphery to the Moderates: Israeli Identity and Foreign Policy in the Middle East. Political Science Quarterly, 130(3), 505–535. <a href="http://www.jstor.org/stable/43828693">Link</a></li>
            <li>Zisser, E. (1995). The Maronites, Lebanon and the State of Israel: Early Contacts. Middle Eastern Studies, 31(4), 889–918. <a href="http://www.jstor.org/stable/4283765">Link</a></li>
        </ul>
        </p>
    </div>
    """,
    folium.Icon(icon='star-of-david', prefix='fa', color='blue')
)



# Save the map
m.save('map.html')
