from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="56856143-888f-5246-a3a8-d9d8f8732b75",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika Chain",
            game_text="This attack does 40 damage for each of your Pikachu and Pikachu ex in play.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)